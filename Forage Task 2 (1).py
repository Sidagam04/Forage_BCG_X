#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load your data
df = pd.read_csv(r"C:\Users\SAI RAM\Downloads\Book1.csv")

# Display the first few rows of the DataFrame
print("Initial Data:")
print(df.head())

# Step 3: Calculate year-over-year changes for each financial metric
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
df['Total Assets Growth (%)'] = df.groupby(['Company'])['Total Assets'].pct_change() * 100
df['Total Liabilities Growth (%)'] = df.groupby(['Company'])['Total Liabilities'].pct_change() * 100
df['Cash Flow Growth (%)'] = df.groupby(['Company'])['Cash Flow from Operating Activities'].pct_change() * 100

# Display the updated DataFrame with growth percentages
print("\nData with Growth Percentages:")
print(df)

# Step 4: Explore aggregate functions or groupings
summary = df.groupby(['Company', 'Year']).agg({
    'Total Revenue': 'sum',
    'Net Income': 'sum',
    'Total Assets': 'sum',
    'Total Liabilities': 'sum',
    'Cash Flow from Operating Activities': 'sum',
    'Revenue Growth (%)': 'mean',
    'Net Income Growth (%)': 'mean',
    'Total Assets Growth (%)': 'mean',
    'Total Liabilities Growth (%)': 'mean',
    'Cash Flow Growth (%)': 'mean'
}).reset_index()

# Display the summary DataFrame
print("\nSummary Data:")
print(summary)

# Step 5: Summarizing findings
# Use markdown cells to document your methodology, observations, and conclusions


# In[9]:


def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue for Microsoft in 2023 is $211 billion, for Tesla is $81 billion, and for Apple is $394 billion."
    elif user_query == "How has net income changed over the last year?":
        return "Microsoft's net income increased by $6.8 billion from 2022 to 2023, Tesla's net income increased by $3 billion, and Apple's net income increased by $20 billion."
    elif user_query == "What are the total assets?":
        return "Microsoft's total assets are $350 billion, Tesla's total assets are $100 billion, and Apple's total assets are $370 billion."
    elif user_query == "What is the cash flow from operating activities?":
        return "Microsoft's cash flow from operating activities is $85 billion, Tesla's is $30 billion, and Apple's is $115 billion."
    elif user_query == "What are the total liabilities?":
        return "Microsoft's total liabilities are $210 billion, Tesla's are $50 billion, and Apple's are $290 billion."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Section 3: Test the Chatbot

print("Welcome to the Financial Analysis Chatbot! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)


# In[ ]:




