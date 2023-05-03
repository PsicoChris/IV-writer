import tkinter
from docxtpl import DocxTemplate



def enter_data():
    doc = DocxTemplate ("V2.docx")

    names_candidate = names_candidate_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    linkedin = linkedin_entry.get()

    full_name= names_candidate + " " + last_name

    city = city_entry.get()
    country = country_entry.get()
    english = english_entry.get()
    phone = phone_entry.get()

    gender_one = gender_one_entry.get()
    gender_two = gender_two_entry.get()

    title = title_entry.get()
    years_of_experience = years_of_experience_entry.get()
    current_company = current_company_entry.get()
    current_role = current_role_entry.get()
    main_techs = main_techs_entry.get()
    other_techs = other_techs_entry.get()

    company_to_apply = company_to_apply_entry.get()

    current_salary = current_salary_entry.get()
    salary_expectation = salary_expectation_entry.get()
    notice_period = notice_period_entry.get()
    other_process = other_process_entry.get()

    context = {'names_candidate':names_candidate, 'lastnames_candidate':last_name, 'email_candidate':email, 'linkedin_candidate':linkedin, 'city_candidate':city, 'country_candidate':country, 'phone_candidate':phone, 'salary_candidate':current_salary, 'salary_expectation_candidate':salary_expectation, 'notice_period_candidate':notice_period, 'other_processs_candidate':other_process, 'english_candidate':english, 'full_name':full_name, 'graduated_title':title, 'years_of_experience':years_of_experience, 'current_company':current_company, 'current_role_actions':current_role, 'gender_for_notes':gender_one, 'gender_for_notes_two':gender_two, 'main_techs':main_techs, 'other_techs':other_techs, 'applying_company':company_to_apply}

    doc.render(context)
    doc.save("doc_final.docx")




window = tkinter.Tk()
window.title("Entry")

frame = tkinter.Frame(window)
frame.pack()

#candidate info
user_info_frame = tkinter.LabelFrame(frame, text="Información del Candidato")
user_info_frame.grid(row= 0, column=0, padx=20, pady=20)


names_candidate_label = tkinter.Label(user_info_frame,text="Nombres")
names_candidate_label.grid(row= 0, column=0)
names_candidate_entry = tkinter.Entry(user_info_frame)
names_candidate_entry.grid(row= 1, column=0)


last_name_label = tkinter.Label(user_info_frame,text="Apellidos")
last_name_label.grid(row= 0, column=1)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row= 1, column=1)


email_label = tkinter.Label(user_info_frame,text="Correo")
email_label.grid(row= 0, column=2)
email_entry = tkinter.Entry(user_info_frame)
email_entry.grid(row= 1, column=2)


linkedin_label = tkinter.Label(user_info_frame,text="LinkedIn")
linkedin_label.grid(row= 0, column=3)
linkedin_entry = tkinter.Entry(user_info_frame)
linkedin_entry.grid(row= 1, column=3)


city_label = tkinter.Label(user_info_frame,text="Ciudad")
city_label.grid(row= 2, column=0)
city_entry = tkinter.Entry(user_info_frame)
city_entry.grid(row= 3, column=0)


country_label = tkinter.Label(user_info_frame,text="País")
country_label.grid(row= 2, column=1)
country_entry = tkinter.Entry(user_info_frame)
country_entry.grid(row= 3, column=1)


english_label = tkinter.Label(user_info_frame,text="Nivel de Inglés")
english_label.grid(row= 2, column=2)
english_entry = tkinter.Entry(user_info_frame)
english_entry.grid(row= 3, column=2)


phone_label = tkinter.Label(user_info_frame,text="Teléfono")
phone_label.grid(row= 2, column=3)
phone_entry = tkinter.Entry(user_info_frame)
phone_entry.grid(row= 3, column=3)


gender_one_label = tkinter.Label(user_info_frame,text="Genero 1 (He/She)")
gender_one_label.grid(row= 4, column=1)
gender_one_entry = tkinter.Entry(user_info_frame)
gender_one_entry.grid(row= 5, column=1)


gender_two_label = tkinter.Label(user_info_frame,text="Genero 2 (His/Her)")
gender_two_label.grid(row= 4, column=2)
gender_two_entry = tkinter.Entry(user_info_frame)
gender_two_entry.grid(row= 5, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




job_info_frame = tkinter.LabelFrame(frame, text="Información Laboral del Candidato")
job_info_frame.grid(row= 1, column=0, padx=20, pady=20)



title_label = tkinter.Label(job_info_frame,text="Título")
title_label.grid(row= 6, column=0)
title_entry = tkinter.Entry(job_info_frame)
title_entry.grid(row= 7, column=0)


years_of_experience_label = tkinter.Label(job_info_frame,text="Años de Experiencia")
years_of_experience_label.grid(row= 6, column=1)
years_of_experience_entry = tkinter.Entry(job_info_frame)
years_of_experience_entry.grid(row= 7, column=1)


current_company_label = tkinter.Label(job_info_frame,text="Compañía Actual")
current_company_label.grid(row= 6, column=2)
current_company_entry = tkinter.Entry(job_info_frame)
current_company_entry.grid(row= 7, column=2)


current_role_label = tkinter.Label(job_info_frame,text="Labores Actuales")
current_role_label.grid(row= 8, column=0)
current_role_entry = tkinter.Entry(job_info_frame)
current_role_entry.grid(row= 9, column=0)


main_techs_label = tkinter.Label(job_info_frame,text="Principales Tecnologías")
main_techs_label.grid(row= 8, column=1)
main_techs_entry = tkinter.Entry(job_info_frame)
main_techs_entry.grid(row= 9, column=1)


other_techs_label = tkinter.Label(job_info_frame,text="Labores Actuales")
other_techs_label.grid(row= 8, column=2)
other_techs_entry = tkinter.Entry(job_info_frame)
other_techs_entry.grid(row= 9, column=2)


company_to_apply_label = tkinter.Label(job_info_frame,text="Labores Actuales")
company_to_apply_label.grid(row= 10, column=1)
company_to_apply_entry = tkinter.Entry(job_info_frame)
company_to_apply_entry.grid(row= 11, column=1)



for widget in job_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)




salary_info_frame = tkinter.LabelFrame(frame, text="Información Salarial del Candidato")
salary_info_frame.grid(row= 2, column=0, padx=20, pady=20)


current_salary_label = tkinter.Label(salary_info_frame,text="Salario Actual")
current_salary_label.grid(row= 12, column=0)
current_salary_entry = tkinter.Entry(salary_info_frame)
current_salary_entry.grid(row= 13, column=0)


salary_expectation_label = tkinter.Label(salary_info_frame,text="Expectativa Salarial")
salary_expectation_label.grid(row= 12, column=1)
salary_expectation_entry = tkinter.Entry(salary_info_frame)
salary_expectation_entry.grid(row= 13, column=1)


notice_period_label = tkinter.Label(salary_info_frame,text="Periodo de Aviso")
notice_period_label.grid(row= 12, column=2)
notice_period_entry = tkinter.Entry(salary_info_frame)
notice_period_entry.grid(row= 13, column=2)


other_process_label = tkinter.Label(salary_info_frame,text="Otros Procesos")
other_process_label.grid(row= 12, column=3)
other_process_entry = tkinter.Entry(salary_info_frame)
other_process_entry.grid(row= 13, column=3)

for widget in salary_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)







button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()