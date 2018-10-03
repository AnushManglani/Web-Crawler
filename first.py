import os


# each website we crawl is new project/folder

def create_project_dir(Directory):
    if not os.path.exists(Directory):
        print("Creating Directory " + Directory)
        os.makedirs(Directory)


# Creating Queue and Crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Creating the FIle
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data in existing files
def add_data(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete data from files
def delete_content(path):
    with open(path, 'w'):
        pass


# convert file to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


# convert set to file
def set_to_file(links, file_name):
    delete_content(file_name)
    for link in sorted(links):
        add_data(file_name, link)

