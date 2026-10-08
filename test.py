"""Sistema de Gestión de Calificaciones Estudiantiles.

Este módulo gestiona los registros de estudiantes, sus calificaciones, promedios,
calificaciones literales, estado de aprobación y estado de honor roll.
"""

GRADE_MIN = 0.0
GRADE_MAX = 100.0
PASSING_GRADE = 60.0
HONOR_ROLL_GRADE = 90.0


class Student:
    """Representa un estudiante y gestiona sus calificaciones académicas."""

    def __init__(self, student_id, name):
        """Inicializa un estudiante con un ID y nombre."""
        if not student_id or not student_id.strip():
            raise ValueError("El ID del estudiante no puede estar vacío.")

        if not name or not name.strip():
            raise ValueError("El nombre del estudiante no puede estar vacío.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.passed = False
        self.honor_roll = False

    def add_grade(self, grade):
        """Agrega una nota válida entre 0 y 100."""
        try:
            numeric_grade = float(grade)
        except (TypeError, ValueError):
            print("Error: La nota debe ser un número.")
            return False

        if not GRADE_MIN <= numeric_grade <= GRADE_MAX:
            print("Error: La nota debe estar entre 0 y 100.")
            return False

        self.grades.append(numeric_grade)
        return True

    def calculate_average(self):
        """Calcula y devuelve el promedio de las calificaciones del estudiante."""
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Devuelve la calificación literal basada en el promedio del estudiante."""
        average = self.calculate_average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def update_status(self):
        """Actualiza el estado de aprobación y el rol de honor."""
        average = self.calculate_average()

        self.passed = average >= PASSING_GRADE
        self.honor_roll = average >= HONOR_ROLL_GRADE

    def remove_grade_by_value(self, grade):
        """Remueve una nota por su valor."""
        try:
            numeric_grade = float(grade)
        except (TypeError, ValueError):
            print("Error: La nota debe ser un número.")
            return False

        if numeric_grade not in self.grades:
            print(f"Error: La nota {numeric_grade} no fue encontrada.")
            return False

        self.grades.remove(numeric_grade)
        return True

    def remove_grade_by_index(self, index):
        """Remueve una nota por su índice."""
        if not isinstance(index, int):
            print("Error: El índice debe ser un número entero.")
            return False

        if index < 0 or index >= len(self.grades):
            print("Error: El índice de la nota está fuera de los límites.")
            return False

        self.grades.pop(index)
        return True

    def report(self):
        """Genera e imprime el informe resumido del estudiante."""
        self.update_status()

        average = self.calculate_average()
        letter_grade = self.get_letter_grade()
        pass_status = "Passed" if self.passed else "Failed"
        honor_status = "Yes" if self.honor_roll else "No"

        print("\n" + "=" * 40)
        print("STUDENT SUMMARY REPORT")
        print("=" * 40)
        print(f"Student ID:       {self.student_id}")
        print(f"Student Name:     {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade:    {average:.2f}")
        print(f"Letter Grade:     {letter_grade}")
        print(f"Pass/Fail:        {pass_status}")
        print(f"Honor Roll:       {honor_status}")
        print("=" * 40)


def main():
    """Ejecuta una demostración del sistema de gestión de calificaciones estudiantiles."""
    try:
        student = Student("ABC001", "Christian Villacres")

        student.add_grade(100)
        student.add_grade(90)
        student.add_grade(85)

        # Ejemplos de notas inválidas.
        student.add_grade("Fifty")
        student.add_grade(150)

        student.report()

        student.remove_grade_by_value(90)

        student.add_grade(95)

        student.report()

        student.remove_grade_by_index(0)

        student.report()

        # Ejemplo de índice inválido.
        student.remove_grade_by_index(99)

    except ValueError as error:
        print(f"Error creando estudiante: {error}")


if __name__ == "__main__":
    main()
