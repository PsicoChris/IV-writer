from docxtpl import DocxTemplate


doc = DocxTemplate ("V2.docx")

names_candidate = input("Names ")
lastnames_candidate = input("Lastnames ")
email_candidate = input("Email ")
linkedin_candidate = input("LinkedIn ")
city_candidate = input("City ")
country_candidate = input("Country ")
phone_candidate = input("Phone number ")
english_candidate = input("English Level ")

full_name = names_candidate + " " + lastnames_candidate

gender_for_notes = input("He/She ")
gender_for_notes_two = input("His/Her ")

graduated_title = input("Degree ")
years_of_experience = input("Years Of Experience ")
current_company = input("Current Company ")
current_role_actions = input("Current Duties ")
main_techs = input("Main Techs ")
other_techs = input("Other Techs ")
applying_company = input("Applying to: ")

salary_candidate = input("Current Salary ")
salary_expectation_candidate = input("Salary Expectation ")
notice_period_candidate = input("Notice Period ")
other_processs_candidate = input("Other Processes ")



context = {'names_candidate':names_candidate, 'lastnames_candidate':lastnames_candidate, 'email_candidate':email_candidate, 'linkedin_candidate':linkedin_candidate, 'city_candidate':city_candidate, 'country_candidate':country_candidate, 'phone_candidate':phone_candidate, 'salary_candidate':salary_candidate, 'salary_expectation_candidate':salary_expectation_candidate, 'notice_period_candidate':notice_period_candidate, 'other_processs_candidate':other_processs_candidate, 'english_candidate':english_candidate, 'full_name':full_name, 'graduated_title':graduated_title, 'years_of_experience':years_of_experience, 'current_company':current_company, 'current_role_actions':current_role_actions, 'gender_for_notes':gender_for_notes, 'gender_for_notes_two':gender_for_notes_two, 'main_techs':main_techs, 'other_techs':other_techs, 'applying_company':applying_company}

doc.render(context)
doc.save("doc_final.docx")