import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Streamlit Advanced Features",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better formatting
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        padding: 20px;
    }
    .section-header {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">Streamlit Advanced Features</h1>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a section:",
    ["Layouts & Formatting", "Columns & Containers", "Tables & DataFrames", 
     "File Upload", "Forms", "User Interactivity", "Data Visualization"]
)

st.sidebar.markdown("---")
st.sidebar.info("Explore advanced Streamlit features")

# Section 1: Layouts and Formatting
if page == "Layouts & Formatting":
    st.header("1. Layouts and Formatting")
    
    st.subheader("Text Formatting Options")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Markdown Formatting")
        st.markdown("**Bold Text**")
        st.markdown("*Italic Text*")
        st.markdown("~~Strikethrough~~")
        st.markdown("`Code snippet`")
        st.markdown("[Link to Streamlit](https://streamlit.io)")
    
    with col2:
        st.markdown("### Special Elements")
        st.success("Success message")
        st.info("Info message")
        st.warning("Warning message")
        st.error("Error message")
    
    st.markdown("---")
    
    st.subheader("Spacing and Dividers")
    st.write("Content before divider")
    st.divider()
    st.write("Content after divider")
    
    st.markdown("---")
    
    st.subheader("Code Blocks")
    code = '''def hello_world():
    print("Hello, Streamlit!")
    return "Success"'''
    st.code(code, language='python')
    
    st.markdown("---")
    
    st.subheader("LaTeX Support")
    st.latex(r'''
        a^2 + b^2 = c^2
    ''')
    st.latex(r'''
        \sum_{i=1}^{n} x_i = x_1 + x_2 + ... + x_n
    ''')

# Section 2: Columns and Containers
elif page == "Columns & Containers":
    st.header("2. Columns and Containers")
    
    st.subheader("Multiple Columns Layout")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Column 1")
        st.write("This is the first column")
        st.button("Button 1")
    
    with col2:
        st.markdown("### Column 2")
        st.write("This is the second column")
        st.button("Button 2")
    
    with col3:
        st.markdown("### Column 3")
        st.write("This is the third column")
        st.button("Button 3")
    
    st.markdown("---")
    
    st.subheader("Columns with Different Widths")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("This column is 2x wider")
        st.info("Width ratio: 2")
    
    with col2:
        st.write("Smaller column")
        st.info("Width ratio: 1")
    
    st.markdown("---")
    
    st.subheader("Containers")
    container1 = st.container()
    container1.write("This is inside a container")
    container1.success("Containers help organize content")
    
    st.write("This is outside the container")
    
    st.markdown("---")
    
    st.subheader("Expanders")
    with st.expander("Click to expand"):
        st.write("Hidden content revealed!")
        st.image("https://via.placeholder.com/400x200", caption="Placeholder Image")
    
    with st.expander("More Information"):
        st.write("Expanders are great for hiding detailed information")
        st.code("st.expander('Title')", language='python')
    
    st.markdown("---")
    
    st.subheader("Tabs")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    
    with tab1:
        st.write("Content in Tab 1")
        st.metric("Metric 1", "100", "+10")
    
    with tab2:
        st.write("Content in Tab 2")
        st.metric("Metric 2", "200", "-5")
    
    with tab3:
        st.write("Content in Tab 3")
        st.metric("Metric 3", "300", "+15")

# Section 3: Tables and DataFrames
elif page == "Tables & DataFrames":
    st.header("3. Displaying Tables and DataFrames")
    
    # Sample data
    data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
        'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories'],
        'Price': [1200, 25, 75, 350, 150],
        'Stock': [50, 200, 150, 75, 100],
        'Rating': [4.5, 4.2, 4.0, 4.7, 4.3]
    }
    df = pd.DataFrame(data)
    
    st.subheader("Interactive DataFrame")
    st.dataframe(df, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Static Table")
    st.table(df)
    
    st.markdown("---")
    
    st.subheader("Styled DataFrame")
    styled_df = df.style.highlight_max(axis=0, color='lightgreen').highlight_min(axis=0, color='lightcoral')
    st.dataframe(styled_df, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("DataFrame with Column Configuration")
    st.dataframe(
        df,
        column_config={
            "Price": st.column_config.NumberColumn(
                "Price (USD)",
                format="$%d"
            ),
            "Rating": st.column_config.ProgressColumn(
                "Rating",
                min_value=0,
                max_value=5,
            ),
        },
        use_container_width=True
    )
    
    st.markdown("---")
    
    st.subheader("Data Editor")
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    
    if st.button("Show Edited Data"):
        st.write("Edited DataFrame:")
        st.write(edited_df)

# Section 4: File Upload
elif page == "File Upload":
    st.header("4. File Upload Widget")
    
    st.subheader("Upload CSV File")
    csv_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if csv_file is not None:
        df_csv = pd.read_csv(csv_file)
        st.success("File uploaded successfully!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Rows", df_csv.shape[0])
        with col2:
            st.metric("Columns", df_csv.shape[1])
        
        st.dataframe(df_csv, use_container_width=True)
        
        st.subheader("Basic Statistics")
        st.write(df_csv.describe())
    
    st.markdown("---")
    
    st.subheader("Upload Excel File")
    excel_file = st.file_uploader("Choose an Excel file", type=['xlsx', 'xls'])
    
    if excel_file is not None:
        df_excel = pd.read_excel(excel_file)
        st.success("Excel file uploaded successfully!")
        st.dataframe(df_excel, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Upload Image")
    image_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    
    if image_file is not None:
        image = Image.open(image_file)
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="Uploaded Image", use_column_width=True)
        
        with col2:
            st.write("Image Details:")
            st.write(f"Format: {image.format}")
            st.write(f"Size: {image.size}")
            st.write(f"Mode: {image.mode}")
    
    st.markdown("---")
    
    st.subheader("Multiple File Upload")
    multiple_files = st.file_uploader("Upload multiple files", accept_multiple_files=True)
    
    if multiple_files:
        st.success(f"Uploaded {len(multiple_files)} files")
        for file in multiple_files:
            st.write(f"- {file.name}")

# Section 5: Forms
elif page == "Forms":
    st.header("5. Creating Forms")
    
    st.subheader("User Registration Form")
    with st.form("registration_form"):
        st.write("Fill in your details:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name")
            email = st.text_input("Email")
            age = st.number_input("Age", min_value=18, max_value=100, value=25)
        
        with col2:
            last_name = st.text_input("Last Name")
            phone = st.text_input("Phone Number")
            country = st.selectbox("Country", ["USA", "UK", "Canada", "Australia", "India"])
        
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        interests = st.multiselect("Interests", ["Sports", "Music", "Reading", "Travel", "Technology"])
        newsletter = st.checkbox("Subscribe to newsletter")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success("Form submitted successfully!")
            st.write("Submitted Data:")
            st.json({
                "Name": f"{first_name} {last_name}",
                "Email": email,
                "Phone": phone,
                "Age": age,
                "Country": country,
                "Gender": gender,
                "Interests": interests,
                "Newsletter": newsletter
            })
    
    st.markdown("---")
    
    st.subheader("Feedback Form")
    with st.form("feedback_form"):
        rating = st.slider("Rate your experience", 1, 5, 3)
        feedback = st.text_area("Your feedback")
        recommend = st.radio("Would you recommend us?", ["Yes", "No", "Maybe"])
        
        submit_feedback = st.form_submit_button("Submit Feedback")
        
        if submit_feedback:
            st.balloons()
            st.success("Thank you for your feedback!")
            st.write(f"Rating: {rating}/5")
            st.write(f"Feedback: {feedback}")
            st.write(f"Recommendation: {recommend}")

# Section 6: User Interactivity
elif page == "User Interactivity":
    st.header("6. Basic User Interactivity")
    
    st.subheader("Session State Management")
    
    if 'counter' not in st.session_state:
        st.session_state.counter = 0
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Increment"):
            st.session_state.counter += 1
    
    with col2:
        if st.button("Decrement"):
            st.session_state.counter -= 1
    
    with col3:
        if st.button("Reset"):
            st.session_state.counter = 0
    
    st.metric("Counter Value", st.session_state.counter)
    
    st.markdown("---")
    
    st.subheader("Dynamic Content")
    
    option = st.selectbox("Choose a category:", ["Technology", "Science", "Sports", "Entertainment"])
    
    content = {
        "Technology": "Latest tech news and innovations",
        "Science": "Scientific discoveries and research",
        "Sports": "Sports updates and scores",
        "Entertainment": "Movies, music, and celebrity news"
    }
    
    st.info(content[option])
    
    st.markdown("---")
    
    st.subheader("Interactive Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num1 = st.number_input("First Number", value=0.0)
    
    with col2:
        operation = st.selectbox("Operation", ["+", "-", "*", "/"])
    
    with col3:
        num2 = st.number_input("Second Number", value=0.0)
    
    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/" and num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
        
        st.success(f"Result: {result}")
    
    st.markdown("---")
    
    st.subheader("Todo List")
    
    if 'todos' not in st.session_state:
        st.session_state.todos = []
    
    new_todo = st.text_input("Add a new task:")
    
    if st.button("Add Task") and new_todo:
        st.session_state.todos.append(new_todo)
        st.success(f"Added: {new_todo}")
    
    if st.session_state.todos:
        st.write("Your Tasks:")
        for i, todo in enumerate(st.session_state.todos):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{i+1}. {todo}")
            with col2:
                if st.button("Delete", key=f"del_{i}"):
                    st.session_state.todos.pop(i)
                    st.rerun()

# Section 7: Data Visualization
elif page == "Data Visualization":
    st.header("7. Simple Data Visualization")
    
    # Generate sample data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=100)
    data_viz = pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(100, 500, 100),
        'Profit': np.random.randint(50, 200, 100),
        'Expenses': np.random.randint(30, 150, 100)
    })
    
    st.subheader("Line Chart")
    st.line_chart(data_viz.set_index('Date')[['Sales', 'Profit', 'Expenses']])
    
    st.markdown("---")
    
    st.subheader("Area Chart")
    st.area_chart(data_viz.set_index('Date')[['Sales', 'Profit']])
    
    st.markdown("---")
    
    st.subheader("Bar Chart")
    monthly_data = data_viz.groupby(data_viz['Date'].dt.month)[['Sales', 'Profit']].sum()
    st.bar_chart(monthly_data)
    
    st.markdown("---")
    
    st.subheader("Plotly Interactive Charts")
    
    tab1, tab2, tab3 = st.tabs(["Scatter Plot", "Pie Chart", "Box Plot"])
    
    with tab1:
        fig_scatter = px.scatter(data_viz, x='Sales', y='Profit', 
                                title='Sales vs Profit',
                                color='Expenses',
                                size='Expenses')
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab2:
        category_data = pd.DataFrame({
            'Category': ['Electronics', 'Clothing', 'Food', 'Books', 'Sports'],
            'Sales': [450, 320, 280, 150, 200]
        })
        fig_pie = px.pie(category_data, values='Sales', names='Category', 
                        title='Sales by Category')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with tab3:
        fig_box = px.box(data_viz, y=['Sales', 'Profit', 'Expenses'],
                        title='Distribution of Metrics')
        st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Matplotlib Charts")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_viz['Date'], data_viz['Sales'], label='Sales', marker='o')
    ax.plot(data_viz['Date'], data_viz['Profit'], label='Profit', marker='s')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount')
    ax.set_title('Sales and Profit Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    st.markdown("---")
    
    st.subheader("Seaborn Heatmap")
    
    corr_data = data_viz[['Sales', 'Profit', 'Expenses']].corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr_data, annot=True, cmap='coolwarm', center=0, ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("### Streamlit Advanced Features - Complete Guide")
st.markdown("Navigate through different sections using the sidebar")
