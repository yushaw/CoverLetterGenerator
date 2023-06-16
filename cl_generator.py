# -*- coding: utf-8 -*-

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
import sys
import os


template = """
    You are an professional {profession}, and you are applying for a job at a company. You are writing a cover letter to apply for the job.
    You need to write a cover letter that is {length} words long. The cover letter should be written in a professional tone. 
    And you are provided with job description and your resume that you can use to write the cover letter, using markdown.

    job description: 
    '''
    {job_description}
    '''

    your resume:
    '''
    {resume}
    '''
    """
    
def generate_cover_letter(openai_api_key, 
                          template = template, 
                          my_resume = "", 
                          profession = "Product Manager", 
                          length = 300,
                          gpt_model = "gpt-4",
                          job_description = "",
                          jd_file_path = ""):
    cl_folder = 'cl'
    jd_abs_path = os.path.join(cl_folder, jd_file_path)
    
    llm = ChatOpenAI(model_name=gpt_model, openai_api_key=openai_api_key, temperature=0.9)
    prompt = PromptTemplate(template=template, input_variables=["profession", "length", "job_description", "resume"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    cl = llm_chain.run({ "profession": profession, "length": length, "job_description": job_description, "resume": my_resume})
       
    try:
        with open(jd_abs_path, 'w', encoding='utf-8') as file:
            file.write(cl)
        print(f"Successfully write to {jd_abs_path}")
    except Exception as e:
        print("Error encountered", str(e))