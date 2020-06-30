import unittest
from turnstile import StateMachine
from turnstile import State


class MyTestCase(unittest.TestCase):

    def setUp(self):
        states = [State("Locked", transitions=[("pass", "Unlocked"), ("enable", "NoEntry")]),
                  State("Unlocked", transitions=[("coin", "Locked"), ("disable", "NoEntry")]),
                  State("NoEntry", transitions=[("disable", "Locked")])]
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

    def test_remain_in_a_locked_state_when_seeing_a_coin(self):
        self.state_machine.transition("coin")
        self.assertEqual("Locked", self.state_machine.current_state.name)

    def test_remain_in_a_unlocked_state_when_seeing_a_pass(self):
        self.state_machine.transition("pass")
        self.state_machine.transition("pass")
        self.assertEqual("Unlocked", self.state_machine.current_state.name)

    def test_can_move_to_a_no_entry_state_from_locked(self):
        self.state_machine.transition("enable")
        self.assertEqual("NoEntry", self.state_machine.current_state.name)

    def test_can_move_to_a_no_entry_state_from_unlocked(self):
        self.state_machine.transition("pass")
        self.state_machine.transition("disable")
        self.assertEqual("NoEntry", self.state_machine.current_state.name)

    def test_can_remain_in_a_no_entry_state_when_seeing_a_pass(self):
        self.state_machine.transition("enable")
        self.state_machine.transition("pass")
        self.assertEqual("NoEntry", self.state_machine.current_state.name)


if __name__ == '__main__':
    unittest.main()
