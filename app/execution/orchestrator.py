import uuid

from app.agents.intent_agent import IntentAgent
from app.agents.workflow_planner_agent import WorkflowPlannerAgent
from app.agents.tool_agent import ToolAgent
from app.execution.tool_registry import ToolRegistry

from app.policy.policy_engine import PolicyEngine
from app.state.state_manager import StateManager
from app.audit.audit_store import audit_store
from app.human.approval_store import approval_store

from app.database.store import save_workflow


class Orchestrator:

    def __init__(self):
        self.intent_agent = IntentAgent()
        self.workflow_agent = WorkflowPlannerAgent()
        self.tool_agent = ToolAgent()
        self.tools = ToolRegistry()

        self.policy = PolicyEngine()
        self.state_manager = StateManager()

    # -------------------------
    # MAIN FLOW
    # -------------------------
    def run(self, user_input: str):

        workflow_id = str(uuid.uuid4())

        audit_store.add("WORKFLOW_STARTED", {
            "workflow_id": workflow_id,
            "input": user_input
        })

        # 1. INTENT DETECTION
        intent = self.intent_agent.detect(user_input)

        audit_store.add("INTENT_DETECTED", {
            "workflow_id": workflow_id,
            "intent": intent
        })

        self.state_manager.create_workflow(workflow_id, intent)

        # 2. APPROVAL FLOW (LOAN ONLY)
        if intent.get("type") == "LOAN_APPLICATION":
            approval_store.create(workflow_id)

            state = self.state_manager.get(workflow_id)
            if state:
                state["pending_input"] = user_input
                state["pending_intent"] = intent

            return {
                "workflow_id": workflow_id,
                "intent": intent,
                "status": "WAITING_FOR_APPROVAL"
            }

        # 3. POLICY CHECK
        policy = self.policy.evaluate(intent)

        audit_store.add("POLICY_CHECK", {
            "workflow_id": workflow_id,
            "policy": policy
        })

        if not policy.get("allowed", False):
            return {
                "workflow_id": workflow_id,
                "intent": intent,
                "policy": policy,
                "execution_result": {"status": "BLOCKED"}
            }

        # 4. TOOL PLANNING
        tool_plan = self.tool_agent.plan(intent)

        audit_store.add("TOOL_PLAN", {
            "workflow_id": workflow_id,
            "tools": tool_plan
        })

        # 5. TOOL EXECUTION
        results = []

        for tool_name in tool_plan:

            if not isinstance(tool_name, str):
                continue

            tool_fn = self.tools.get(tool_name)

            if not tool_fn:
                results.append({
                    "step": tool_name,
                    "status": "FAILED",
                    "result": "Tool not found"
                })
                continue

            try:
                output = tool_fn()

                results.append({
                    "step": tool_name,
                    "status": "SUCCESS",
                    "result": output
                })

                self.state_manager.add_step(workflow_id, tool_name)

            except Exception as e:
                results.append({
                    "step": tool_name,
                    "status": "FAILED",
                    "result": str(e)
                })

        execution_result = {
            "status": "COMPLETED",
            "steps": results
        }

        self.state_manager.complete(workflow_id)

        audit_store.add("WORKFLOW_COMPLETED", {
            "workflow_id": workflow_id,
            "result": execution_result
        })

        save_workflow(workflow_id, intent, execution_result)

        return {
            "workflow_id": workflow_id,
            "intent": intent,
            "policy": policy,
            "execution_result": execution_result
        }

    # -------------------------
    # RESUME FLOW
    # -------------------------
    def resume(self, workflow_id: str):

        workflow = self.state_manager.get_workflow(workflow_id)

        if not workflow:
            return {"error": "Workflow not found"}

        intent = workflow.get("pending_intent", workflow.get("intent"))
        user_input = workflow.get("pending_input")

        if not user_input:
            return {
                "workflow_id": workflow_id,
                "error": "No pending input"
            }

        tool_plan = self.tool_agent.plan(intent)

        results = []

        for item in tool_plan:

            # SAFE EXTRACTION
            if isinstance(item, dict):
                tool_name = item.get("tool") or item.get("name")
            else:
                tool_name = item

            if not isinstance(tool_name, str):
                continue

            tool_fn = self.tools.get(tool_name)

            if not tool_fn:
                continue

            try:
                results.append({
                    "step": tool_name,
                    "status": "SUCCESS",
                    "result": tool_fn()
                })

            except Exception as e:
                results.append({
                    "step": tool_name,
                    "status": "FAILED",
                    "result": str(e)
                })

        return {
            "workflow_id": workflow_id,
            "status": "RESUMED",
            "steps": results
        }