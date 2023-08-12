import streamlit as st
import os

st.markdown(
        """
        <style>
        body {
            color: #262730;
            background-color: #FFFFFF;
            font-family: sans-serif;
        }
        .stButton button {
            background-color: #F63366;
            color: #FFFFFF;
        }
        .stButton button:hover {
            background-color: #FF7091;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    st.title("Shubham Dipak Kamble's Portfolio")
    
    st.sidebar.subheader("Contact Information")
    st.sidebar.markdown("Email: shubhamkamble7003@gmail.com\n\nContact No: 7972799088\n\nLocation: Pune, India")


    #st.markdown("Contact No: 7972799088")
    #st.markdown("Location: Pune, India")
    
    st.sidebar.markdown("### Bio")
    st.sidebar.markdown("I am a data analyst specializing in creating impactful visualizations using Power BI. I am proficient in utilizing tools such as MySQL for data manipulation and have a solid grasp of Python for data analysis. I am enthusiastic about generative AI tools and skilled in building web applications using Streamlit and ChatGPT.")
    st.sidebar.markdown("### Profile Links")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/shubham-kamble-9b0867172/)")
    st.sidebar.markdown("[YouTube](https://www.youtube.com/@shubhamkamble6914/featured)")
    st.sidebar.markdown("[Google Cloud](https://www.cloudskillsboost.google/public_profiles/5903b42b-5480-45dd-8f48-397969e4baac)")
    st.sidebar.markdown("[GitHub](https://github.com/sdk1728)")
    
    st.subheader("Professional Experience")
    st.markdown("**Data Analyst Intern**")
    st.markdown("Yoshops.com")
    st.markdown("01/2023 to 03/2023")
    st.markdown("""• Conducted web scraping on multiple E-commerce websites such as Reliance Digital, Vijay Sales, Amazon, Flipkart, and
                    HRX to collect valuable data.
                    • Analysed the collected data to understand the sales trends and customer reviews.
                    • Developed a visually appealing and insightful Power-Bi dashboard to present the analysed data to stakeholders.
                    • Successfully communicated the key findings and recommendations to improve product sales and customer experience.""")

    show_power_bi_projects = st.button("Power BI Projects")

    if show_power_bi_projects:
        st.subheader("Power BI Projects")

        projects_folder = "power_bi_dashboards"

        # List files in the projects folder
        project_files = os.listdir(projects_folder)

        for file in project_files:
            if file.endswith(".png"):
                project_name = os.path.splitext(file)[0]
                project_image_path = os.path.join(projects_folder, file)
                project_link = f"https://app.powerbi.com/groups/me/reports/{project_name}/ReportSection?experience=power-bi"

                st.markdown(f"**{project_name.replace('_', ' ').title()}**")
                st.image(project_image_path, use_column_width=True)
                st.markdown(f"[Open Power BI Report]({project_link})")
    


    

    
                
    
    # Repeat the same structure for the rest of your resume sections

if __name__ == "__main__":
    main()
