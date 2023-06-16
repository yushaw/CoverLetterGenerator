# -*- coding: utf-8 -*-

import cl_generator
import os

# variables
openai_api_key= os.environ.get('OPENAI_API_KEY') # replace with your own API key
my_resume = ""
profession = "Product Manager"
gpt_model = "gpt-4"
length = 300
template = """
    You are an professional {profession}, and you are applying for a job at a company. You are writing a cover letter to apply for the job.
    You need to write a cover letter that is {length} words long. The cover letter should be written in a professional tone. 
    And you are provided with job description and your resume that you can use to write the cover letter, using markdown.
    Your cover letter start with:
    '''
    Dear [Recipient's Name],
    ...
    '''
    
    
    job description: 
    '''
    {job_description}
    '''

    your resume:
    '''
    {resume}
    '''
    
    """

try:
    with open('Resume.md', 'r', errors='ignore') as f:
        my_resume = f.read()
except FileNotFoundError:
    print("File not found")
    sys.exit()


# check folder jd and cl
jd_folder = 'jd'
cl_folder = 'cl'

jd_files = os.listdir(jd_folder)

for jd_file in jd_files:
    cl_file_path = os.path.join(cl_folder, jd_file)
    
    if os.path.isfile(cl_file_path):
        print(f"File {cl_file_path} already exists")
        continue
    
    jd_file_path = os.path.join(jd_folder, jd_file)
    
    with open(jd_file_path, 'r', errors='ignore') as f:
        job_description = f.read()

    cl_generator.generate_cover_letter(openai_api_key=openai_api_key, 
                                   template=template,
                                   my_resume=my_resume,
                                   profession=profession,
                                   length=length,
                                   gpt_model=gpt_model,
                                   job_description=job_description,
                                   jd_file_path=jd_file)