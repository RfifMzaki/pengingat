document.addEventListener("DOMContentLoaded", function () {
    const container = document.getElementById("ulang_tahun_container");
    const nextButton = document.getElementById("next-btn");
    const prevButton = document.getElementById("prev-btn");
    let index = 0;
    let dataUlangTahun = getDataUlangTahun();

    // Fungsi untuk mengambil data ulang tahun dari server atau sumber data lainnya
    function getDataUlangTahun() {
        // Ganti dengan logika pengambilan data ulang tahun dari server atau sumber data lainnya
        return [
            { name: "Khaira", birthday: "1 Januari" },
            { name: "Fiona", birthday: "2 Januari" },
            { name: "Kintan", birthday: "28 Maret" },
            { name: "Daffa", birthday: "15 Mei" },
            { name: "Nabylla", birthday: "18 Juli" },
            { name: "Aura", birthday: "7 September" },
            { name: "Farah", birthday: "19 Desember" },
            { name: "Rafif", birthday: "23 Desember" },
            // ...Tambahkan data teman lainnya sesuai kebutuhan
        ];
    }

    // Fungsi untuk menampilkan data ulang tahun pada container
    function displayBirthday(index) {
        const upcomingBirthday = dataUlangTahun[index];
        if (upcomingBirthday) {
            const text = `${upcomingBirthday.name}: ${upcomingBirthday.birthday}`;
            container.innerHTML = text;
        } else {
            container.innerHTML = "Tidak ada ulang tahun yang akan datang.";
        }
    }

    // Fungsi untuk menampilkan animasi pengingat ulang tahun
    function showBirthdayAnimation() {
        displayBirthday(index);

        // Tambahkan event listener untuk tombol selanjutnya dan sebelumnya
        nextButton.addEventListener("click", function () {
            index = (index + 1) % dataUlangTahun.length;
            displayBirthday(index);
        });

        prevButton.addEventListener("click", function () {
            index = (index - 1 + dataUlangTahun.length) % dataUlangTahun.length;
            displayBirthday(index);
        });
    }

    // Panggil fungsi untuk menampilkan animasi saat dokumen selesai dimuat
    showBirthdayAnimation();
});