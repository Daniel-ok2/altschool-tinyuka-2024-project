import uuid
from datetime import datetime

# Expense Class
class Expense:
    def __init__(self, title: str, amount: float):
        """Initialize an Expense object with a title and amount."""
        self.id = str(uuid.uuid4())  # Generate a unique UUID string
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Current UTC timestamp
        self.updated_at = self.created_at  # Initially same as created_at

    def update(self, title: str = None, amount: float = None):
        """Update title and/or amount, and set updated_at to current UTC time."""
        if title is not None:
            self.title = title
        if amount is not None:
            self.amount = amount
        if title is not None or amount is not None:  # Update timestamp only if changes occur
            self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Return a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),  # ISO format for readability
            "updated_at": self.updated_at.isoformat()
        }


# ExpenseDatabase Class
class ExpenseDatabase:
    def __init__(self):
        """Initialize an empty list to store expenses."""
        self.expenses = []

    def add_expense(self, expense: Expense):
        """Add an Expense object to the database."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """Remove an expense from the database by its ID."""
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieve an expense by its ID, or None if not found."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title: str):
        """Retrieve a list of expenses matching the given title."""
        return [exp for exp in self.expenses if exp.title == title]

    def to_dict(self):
        """Return a list of dictionaries representing all expenses."""
        return [expense.to_dict() for expense in self.expenses]


# Example Usage (for testing)
if __name__ == "__main__":
    # Create an ExpenseDatabase instance
    db = ExpenseDatabase()

    # Add some expenses
    exp1 = Expense("Groceries", 50.75)
    exp2 = Expense("Rent", 1200.00)
    db.add_expense(exp1)
    db.add_expense(exp2)

    # Update an expense
    exp1.update(title="Supermarket", amount=60.00)

    # Test retrieval
    print("Expense by ID:", db.get_expense_by_id(exp1.id).to_dict())
    print("Expenses by title 'Rent':", [e.to_dict() for e in db.get_expense_by_title("Rent")])
    print("All expenses:", db.to_dict())

    # Remove an expense
    db.remove_expense(exp2.id)
    print("After removal:", db.to_dict())