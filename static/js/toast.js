let toastTimer;

function showToast(title, message, type = "normal", duration = 3000) {
    const toastComponent = document.getElementById("toast-component");
    const toastTitle = document.getElementById("toast-title");
    const toastMessage = document.getElementById("toast-message");

    if (!toastComponent || !toastTitle || !toastMessage) {
        console.error("Toast component tidak ditemukan.");
        return;
    }

    // Hapus class tipe sebelumnya
    toastComponent.classList.remove(
        "toast-success",
        "toast-error",
        "toast-normal"
    );

    // Tambahkan class sesuai tipe
    if (type === "success") {
        toastComponent.classList.add("toast-success");
    } else if (type === "error") {
        toastComponent.classList.add("toast-error");
    } else {
        toastComponent.classList.add("toast-normal");
    }

    // Update isi toast
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Batalkan timer sebelumnya
    clearTimeout(toastTimer);

    // Pastikan toast terbuka
    if (!toastComponent.matches(":popover-open")) {
        try {
            toastComponent.showPopover();
        } catch (error) {
            console.error("Gagal membuka toast:", error);
            return;
        }
    }

    // Reset state animasi
    toastComponent.classList.remove("toast-hidden");

    // Paksa browser menghitung ulang style
    void toastComponent.offsetHeight;

    // Tampilkan toast
    toastComponent.classList.add("toast-show");

    // Sembunyikan setelah durasi
    toastTimer = setTimeout(() => {
        toastComponent.classList.remove("toast-show");
        toastComponent.classList.add("toast-hidden");

        setTimeout(() => {
            if (toastComponent.matches(":popover-open")) {
                toastComponent.hidePopover();
            }
        }, 300);
    }, duration);
}