class Application:
    def __init__(self, repository, json_loader, serializer, extension):
        self.repository = repository
        self.json_loader = json_loader
        self.serializer = serializer
        self.extension = extension

    def run(self, rooms_path, students_path):        
        # Load data
        rooms = self.json_loader.load_json(rooms_path)
        students = self.json_loader.load_json(students_path)

        # Insert data into repository
        self.repository.insert_rooms(rooms)
        self.repository.insert_students(students)

        # Run database queries
        task_1 = self.repository.get_rooms_with_student_count()
        task_2 = self.repository.get_5_rooms_with_smallest_average_age()
        task_3 = self.repository.get_5_rooms_with_largest_age_difference()
        task_4 = self.repository.rooms_with_different_sex_students()

        # Save query results 
        self.serializer.save(task_1, f"task_1.{self.extension}")
        self.serializer.save(task_2, f"task_2.{self.extension}")
        self.serializer.save(task_3, f"task_3.{self.extension}")
        self.serializer.save(task_4, f"task_4.{self.extension}")
        