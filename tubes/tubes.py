import os
from datetime import datetime, timedelta

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
        print("5. Urutkan Tugas berdasarkan Deadline")
        print("6. Perbarui Tugas")
        print("7. Hapus Tugas")
        print("8. Keluar")

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

        elif choice == '5':
            if not tasks:
                print("Belum ada tugas yang ditambahkan.")
            else:
                sorted_tasks = sorted(tasks, key=lambda x: datetime.strptime(x.deadline, "%Y-%m-%d"))
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n=======Daftar Tugas Urut berdasarkan Deadline=======")
                for idx, task in enumerate(sorted_tasks, 1):
                    print(f"Tugas {idx}:")
                    task.display_info()

        elif choice == '6':
            if not tasks:
                print("Belum ada tugas yang ditambahkan.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n=======Daftar Tugas=======")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.name}")

                task_index = int(input("Masukkan nomor tugas yang ingin diperbarui: "))
                if 1 <= task_index <= len(tasks):
                    task = tasks[task_index - 1]
                    print(f"\nData Tugas saat ini:")
                    task.display_info()

                    print("\nMasukkan data baru untuk tugas ini:")
                    name = input("Masukkan nama tugas baru (tekan Enter untuk tidak mengubah): ") or task.name
                    deadline = input("Masukkan deadline baru (tekan Enter untuk tidak mengubah): ") or task.deadline
                    description = input("Masukkan deskripsi tugas baru (tekan Enter untuk tidak mengubah): ") or task.description
                    subject = input("Masukkan mata pelajaran baru (tekan Enter untuk tidak mengubah): ") or task.subject

                    task.name = name
                    task.deadline = deadline
                    task.description = description
                    task.subject = subject

                    print("Tugas berhasil diperbarui.")
                else:
                    print("Nomor tugas tidak valid.")

        elif choice == '7':
            if not tasks:
                print("Belum ada tugas yang ditambahkan.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n=======Daftar Tugas=======")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.name}")

                task_index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                if 1 <= task_index <= len(tasks):
                    deleted_task = tasks.pop(task_index - 1)
                    print(f"Tugas '{deleted_task.name}' berhasil dihapus.")
                else:
                    print("Nomor tugas tidak valid.")

        elif choice == '8':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Program telah selesai atau dihentikan.")
            break
        

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()