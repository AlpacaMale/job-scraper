def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Title,Company,Region,URL\n")

    for job in jobs:
        file.write(f"{job['title']},{job['company']},{job['region']},{job['link']}\n")
    file.close()
