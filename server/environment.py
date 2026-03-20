import uuid
from models import Action, Observation, StepResult, State

class CodingEnvironment:
    def __init__(self):
        self.episode_id = str(uuid.uuid4())
        self.step_count = 0
        
        self.problem = "Write a function add(a, b) that returns sum."

        self.test_cases = [
            (1, 2, 3),
            (5, 7, 12),
            (10, -2, 8)
        ]

    def reset(self):
        self.step_count = 0
        return StepResult(
            observation=Observation(
                problem=self.problem,
                feedback="Start coding"
            ),
            reward=0.0,
            done=False
        )

    def step(self, action: Action):
        self.step_count += 1

        passed = 0
        total = len(self.test_cases)

        try:
            local_env = {}
            exec(action.code, {}, local_env)

            func = local_env.get("add")

            for a, b, expected in self.test_cases:
                if func(a, b) == expected:
                    passed += 1

            reward = passed / total

            feedback = f"{passed}/{total} test cases passed"

        except Exception as e:
            reward = 0
            feedback = f"Error: {str(e)}"

        done = True  # one-shot problem

        return StepResult(
            observation=Observation(
                problem=self.problem,
                feedback=feedback
            ),
            reward=reward,
            done=done
        )

    @property
    def state(self):
        return State(
            step_count=self.step_count,
            episode_id=self.episode_id
        )