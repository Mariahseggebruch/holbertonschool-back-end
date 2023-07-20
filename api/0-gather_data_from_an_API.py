import requests

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    users_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetching data from the API
        todos_response = requests.get(todos_url)
        users_response = requests.get(users_url)
        todos_data = todos_response.json()
        users_data = users_response.json()

        # Extracting relevant information
        employee_name = users_data["name"]
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo["completed"])
        completed_titles = [todo["title"] for todo in todos_data if todo["completed"]]

        # Displaying the information
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        for title in completed_titles:
            print("\t" + title)

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data from the API:", e)
    except KeyError:
        print("Invalid employee ID. Please provide a valid integer as the employee ID.")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

