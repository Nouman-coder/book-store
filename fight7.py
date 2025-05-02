import streamlit as st

# Initialize book data
if "book_ids" not in st.session_state:
    st.session_state.book_ids = [1, 2, 3, 4, 5]
    st.session_state.titles = ["Python Basics", "AI & ML", "Data Science", "Web Development", "Cyber Security"]
    st.session_state.stocks = [10, 5, 8, 6, 4]
    st.session_state.prices = [250, 400, 300, 350, 500]

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

# Title
st.title("📚 Python Book Store")

# Sidebar menu
choice = st.sidebar.selectbox("Select an Option", ["Show All Books", "Buy a Book", "Add New Book (Admin Only)"])

# Option 1: Show All Books
if choice == "Show All Books":
    st.header("📖 Available Books")
    for i in range(len(st.session_state.book_ids)):
        st.write(f"**{st.session_state.book_ids[i]}. {st.session_state.titles[i]}**")
        st.write(f"Stock: {st.session_state.stocks[i]}")
        st.write(f"Price: Rs.{st.session_state.prices[i]}")
        st.markdown("---")

# Option 2: Buy a Book
elif choice == "Buy a Book":
    st.header("🛒 Buy a Book")

    # Filter books with stock > 0
    available_books = [
        f"{book_id}. {title} (Stock: {stock}) - Rs.{price}"
        for book_id, title, stock, price in zip(
            st.session_state.book_ids,
            st.session_state.titles,
            st.session_state.stocks,
            st.session_state.prices
        ) if stock > 0
    ]

    if available_books:
        selected_book = st.selectbox("Select a book to buy:", available_books)
        book_id = int(selected_book.split(".")[0])
        index = st.session_state.book_ids.index(book_id)

        name = st.text_input("Enter your name:")
        confirm = st.checkbox(f"I confirm I want to buy '{st.session_state.titles[index]}' for Rs.{st.session_state.prices[index]}")

        if st.button("Buy Now"):
            if not name:
                st.warning("Please enter your name.")
            elif not confirm:
                st.warning("Please confirm your purchase.")
            else:
                st.session_state.stocks[index] -= 1
                st.success("Purchase successful!")

                st.markdown("### 🧾 Bill")
                st.write(f"**Customer:** {name}")
                st.write(f"**Book:** {st.session_state.titles[index]}")
                st.write(f"**Amount:** Rs.{st.session_state.prices[index]}")
    else:
        st.error("❌ All books are currently out of stock.")

# Option 3: Add New Book 
elif choice == "Add New Book (Admin Only)":
    st.header("🔒 Admin Panel")

    # Track login status in session_state
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        username = st.text_input("Enter admin username")
        password = st.text_input("Enter admin password", type="password")
        if st.button("Login"):
            if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                st.session_state.admin_logged_in = True
                st

