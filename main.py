import streamlit as st
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent 
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

def main():
    
    load_dotenv()   

    st.set_page_config(page_title="Talk to your CSV 📈")
    st.header("Talk to your CSV 📈")

    user_csv = st.file_uploader("Upload your CSV file", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask a question about your CSV: ")

        llm = OpenAI(temperature=0)
        agent = create_csv_agent(llm, user_csv, verbose=True) # verbose=True prints the model thinking in green text.

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()
