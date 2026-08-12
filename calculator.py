import math
from typing import Union, List, Dict, Callable

class InvalidOperatorError(Exception):
    """Custom exception raised when an unsupported mathematical operation is requested."""
    pass

class NegativeRootError(Exception):
    """Custom exception raised when taking the square root of a negative value."""
    pass

class Calculator:
    """A secure, object-oriented calculation engine with history capabilities and exception isolation."""

    def __init__(self) -> None:
        self._history: List[str] = []
        # Mapping operators to structural helper methods
        self._operations: Dict[str, Callable] = {
            '+': self._add,
            '-': self._subtract,
            '*': self._multiply,
            '/': self._divide,
            '^': self._power,
            '%': self._modulo,
            'sqrt': self._square_root
        }

    def _validate_numeric(self, *args: any) -> None:
        """Internal assertion layer verifying variables contain proper integer or floating-point datatypes."""
        for arg in args:
            if not isinstance(arg, (int, float)) or isinstance(arg, bool):
                raise TypeError(f"Invalid input type: '{type(arg).__name__}'. Operands must be strictly numeric.")

    def _add(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        return a + b

    def _subtract(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        return a - b

    def _multiply(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        return a * b

    def _divide(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        if b == 0:
            raise ZeroDivisionError("Division Error: Denominator evaluates to absolute zero.")
        return a / b

    def _power(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        try:
            return math.pow(a, b)
        except OverflowError:
            raise OverflowError("Arithmetic Overflow: Exponential result grows too large for system thresholds.")

    def _modulo(self, a: float, b: float) -> float:
        self._validate_numeric(a, b)
        if b == 0:
            raise ZeroDivisionError("Modulo Error: Attempted remainder calculation against a zero divisor.")
        return a % b

    def _square_root(self, a: float) -> float:
        self._validate_numeric(a)
        if a < 0:
            raise NegativeRootError("Domain Error: Cannot extract real-number square roots from negative numbers.")
        return math.sqrt(a)

    def execute(self, operator: str, *args: any) -> Union[float, str]:
        """
        Runs equations within a central try-except runtime shield.
        Automatically commits successful transactions into the audit trail ledger.
        """
        try:
            op_clean = operator.strip().lower()
            if op_clean not in self._operations:
                raise InvalidOperatorError(f"Unsupported mathematical operation symbol: '{operator}'.")

            # Dynamically look up operation routine and unpack variable arguments
            result = self._operations[op_clean](*args)

            # Log clean human-readable entry depending on math parity structures
            if op_clean == 'sqrt':
                log_entry = f"sqrt({args[0]}) = {result}"
            else:
                log_entry = f"{args[0]} {op_clean} {args[1]} = {result}"
            
            self._history.append(log_entry)
            return result

        except ZeroDivisionError as zde:
            return f"[Math Error] {zde}"
        except TypeError as te:
            return f"[Type Error] {te}"
        except InvalidOperatorError as ioe:
            return f"[Operator Error] {ioe}"
        except NegativeRootError as nre:
            return f"[Domain Error] {nre}"
        except OverflowError as ofe:
            return f"[Overflow Error] {ofe}"
        except Exception as general_fault:
            return f"[Unexpected Structural Fault] Exception bypassed safely: {general_fault}"

    def get_history(self) -> List[str]:
        """Retrieves history tracking array."""
        return self._history

    def clear_history(self) -> None:
        """Purges active calculation registry indexes cleanly."""
        self._history.clear()


def run_cli_loop() -> None:
    """Spawns an input-buffered interactive command-line workspace loop."""
    calc = Calculator()
    print("==================================================")
    print("     ENTERPRISE CLI CALCULATOR WORKSPACE SYSTEM   ")
    print("==================================================")

    while True:
        print("\nAvailable Operations Index:")
        print(" [ + ] Add        [ - ] Subtract    [ * ] Multiply")
        print(" [ / ] Divide     [ ^ ] Exponent    [ % ] Modulo")
        print(" [ sqrt ] Root    [ H ] View Log    [ C ] Clear Log")
        print(" [ Q ] Exit System")

        user_input = input("\nSelect token action or operator: ").strip()
        action = user_input.lower()

        if action == 'q':
            print("\nDeallocating runtime instances safely. Session terminated cleanly.")
            break
        elif action == 'h':
            logs = calc.get_history()
            print("\n--- Operational Audit Logs ---")
            if not logs:
                print("No transactions verified inside ledger.")
            else:
                for index, entry in enumerate(logs, 1):
                    print(f" Record #{index:02d}: {entry}")
            print("------------------------------")
            continue
        elif action == 'c':
            calc.clear_history()
            print("\n[System Alert] Audit log history wiped successfully.")
            continue
        elif action not in ['+', '-', '*', '/', '^', '%', 'sqrt']:
            print("\n[Input Warning] Unknown option identifier. Resetting execution step.")
            continue

        try:
            if action == 'sqrt':
                num_str = input("Enter operand value: ").strip()
                val = float(num_str)
                output = calc.execute(action, val)
                print(f"\nExecution Output: {output}")
            else:
                num1_str = input("Enter first operand: ").strip()
                num2_str = input("Enter second operand: ").strip()
                val1 = float(num1_str)
                val2 = float(num2_str)
                output = calc.execute(action, val1, val2)
                print(f"\nExecution Output: {output}")
        except ValueError:
            print("\n[Parsing Error] Local buffer intercepted an invalid literal format. Type numerical digits only.")


if __name__ == "__main__":
    run_cli_loop()