import os

class Task:
    def __init__(self, name, deadline, description, subject):
        self.name = name
        self.deadline = deadline
        self.description = description
        self.subject = subject

    def display_info(self):
        print(f"Nama Tugas: {self.name}")
        print(f"Deadline: {self.deadline}")
        print(f"Deskripsi: {self.description}")
        print(f"Mata Pelajaran: {self.subject}\n")


def main():
    tasks = []  # Inisialisasi list untuk menyimpan tugas-tugas

    while True:
        
        print("\nMenu Tugas:")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Cari Tugas berdasarkan Mata Pelajaran")
        print("4. Urutkan Tugas berdasarkan Mata Pelajaran")

        choice = input("Pilih menu: ")

        if choice == '1':
            name = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline (contoh: 2024-12-31): ")
            description = input("Masukkan deskripsi tugas: ")
            subject = input("Masukkan mata pelajaran: ")

            task = Task(name, deadline, description, subject)
            tasks.append(task)
            print("Tugas berhasil ditambahkan!")

        elif choice == '2':
            if not tasks:
                print("Belum ada tugas yang ditambahkan.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n=======Daftar Tugas=======")
                for idx, task in enumerate(tasks, 1):
                    print(f"Tugas {idx}:")
                    task.display_info()

        elif choice == '3':
            subject_search = input("Masukkan mata pelajaran yang ingin dicari: ")
            found_tasks = [task for task in tasks if task.subject.lower() == subject_search.lower()]

            if not found_tasks:
                print(f"Tidak ada tugas dengan mata pelajaran '{subject_search}'.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n=======Tugas dengan Mata Pelajaran '{subject_search}'=======")
                for task in found_tasks:
                    task.display_info()

        elif choice == '4':
            sorted_tasks = sorted(tasks, key=lambda x: x.subject.lower())
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n=======Daftar Tugas Urut berdasarkan Mata Pelajaran=======")
            for idx, task in enumerate(sorted_tasks, 1):
                print(f"Tugas {idx}:")
                task.display_info()

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
