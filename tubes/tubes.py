import os

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def display_info(self):
        print(f"Nama Tugas: {self.name}")
        print(f"Deadline: {self.deadline}")


def main():
    tasks = []  # Inisialisasi list untuk menyimpan tugas-tugas

    while True:
        
        print("\nMenu Tugas:")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            name = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline (contoh: 2024-12-31): ")

            task = Task(name, deadline)
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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Program telah selesai atau dihentikan.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
