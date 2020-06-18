import unittest
from turnstile import StateMachine
from turnstile import State


class MyTestCase(unittest.TestCase):

    def setUp(self):
        states = [State("Locked", "pass", "Unlocked"), State("Unlocked", "coin", "Locked")]
        self.state_machine = StateMachine(
            states=states,
            initial_state=states[0]
        )

    def test_framework_is_working(self):
        self.assertEqual(True, True)

    def test_turnstile_exists(self):
        self.assertIsInstance(self.state_machine, StateMachine)

    def test_initial_state_is_locked(self):
        self.assertEqual("Locked", self.state_machine.initial_state.name)

    def test_initial_state_changes_when_given_a_pass(self):
        self.state_machine.transition("pass")
        self.assertEqual("Unlocked", self.state_machine.current_state.name)

    def test_can_move_back_to_initial_state(self):
        self.state_machine.transition("pass")
        self.assertEqual("Unlocked", self.state_machine.current_state.name)
        self.state_machine.transition("coin")
        self.assertEqual("Locked", self.state_machine.current_state.name)


if __name__ == '__main__':
    unittest.main()
