from typing import List

class Product:
    """
    Represents an individual product purchased by a customer.
    Encapsulates structural state such as name, unit price, and acquisition quantity.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        """Calculates the total localized item cost based on price and item volume."""
        return self.price * self.quantity


class Bill:
    """
    Responsible for collection tracking, managing subtotal allocations,
    calculating fiscal tax duties, and rendering finalized tabular invoices.
    """
    def __init__(self, tax_rate: float = 0.15) -> None:
        self.products: List[Product] = []
        self.tax_rate = tax_rate  # Expected as a fractional float multiplier (e.g., 0.15 for 15%)

    def add_product(self, product: Product) -> None:
        """Appends a validated Product class object to the internal tracking system ledger."""
        if not isinstance(product, Product):
            raise TypeError("Operation Rejected: Object must be a valid instance of the Product class.")
        self.products.append(product)

    def calculate_subtotal(self) -> float:
        """Aggregates individual cumulative pricing vectors across all added items before tax applied."""
        return sum(item.total_price for item in self.products)

    def calculate_tax(self) -> float:
        """Computes total applicable sales tax based on the cumulative transaction subtotal."""
        return self.calculate_subtotal() * self.tax_rate

    def calculate_final_total(self) -> float:
        """Calculates total customer financial liability combining net subtotal and tax amounts."""
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self) -> None:
        """
        Renders a cleanly formatted tabular receipt to standard output,
        ensuring alignment across product descriptions and structural monetary fields.
        """
        if not self.products:
            print("\n" + "!" * 50)
            print("      INVOICE GENERATION FAILED: LEDGER EMPTY      ")
            print("!" * 50)
            print("Action Required: Please append valid items prior to billing execution.")
            return

        print("\n" + "=" * 65)
        print(f"{'CUSTOMER TRANSACTION INVOICE':^65}")
        print("=" * 65)
        
        # Tabular header aligned perfectly to meet formatting parameters
        print(f"{'Product':<25} {'Price':<12} {'Quantity':<12} {'Total':<12}")
        print("-" * 65)
        
        # Dynamically generate line item records
        for item in self.products:
            print(f"{item.name:<25} ${item.price:<11.2f} {item.quantity:<12} ${item.total_price:<11.2f}")
            
        print("-" * 65)
        
        # Compute summary values
        subtotal = self.calculate_subtotal()
        tax_amount = self.calculate_tax()
        final_payable = self.calculate_final_total()
        
        # Display summarized financial outputs
        print(f"{'Subtotal:':<51} ${subtotal:.2f}")
        print(f"{f'Tax ({self.tax_rate * 100:.1f}%):':<51} ${tax_amount:.2f}")
        print("=" * 65)
        print(f"{'Final Payable Amount:':<51} ${final_payable:.2f}")
        print("=" * 65)


# =====================================================================
# SYSTEM VERIFICATION AND OPERATIONAL TESTING BLOCK
# =====================================================================
if __name__ == "__main__":
    # Initialize a retail customer bill with a configured 12.5% tax bracket rate
    invoice = Bill(tax_rate=0.125)
    
    # Create concrete instance variations of Product structures
    item_a = Product("Ergonomic Desk Chair", 149.99, 1)
    item_b = Product("Anker USB-C Docking Hub", 64.50, 2)
    item_c = Product("Matte Screen Protector", 15.25, 3)
    item_d = Product("Logitech MX Master Mouse", 99.00, 1)
    
    # Populate billing architecture item lists
    invoice.add_product(item_a)
    invoice.add_product(item_b)
    invoice.add_product(item_c)
    invoice.add_product(item_d)
    
    # Process computation algorithms and display final summary dashboard
    invoice.display_bill()
