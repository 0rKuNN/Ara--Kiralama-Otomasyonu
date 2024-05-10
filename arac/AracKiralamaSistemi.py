import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime, timedelta
import random
from PIL import Image, ImageTk
import os

class AracKiralamaSistemi:
    def __init__(self, root):
        self.root = root
        self.root.title("Araç Kiralama Uygulaması")
        self.root.geometry("610x400")

        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill="both")

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="arac_kiralama"
        )
        self.cursor = self.conn.cursor()

        self.root.configure(bg="black")

        self.kullanici_id = None
        self.giris_sayfasi()

    def giris_sayfasi(self):
        if hasattr(self, "frame"):
            self.frame.destroy()

        self.kullanici_id = None

        self.frame = tk.Frame(self.root, bg="black")
        self.frame.pack(expand=True, fill="both")

        image_path = ("C:/Users/orkun/aracc.jpg")
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)

            background_label = tk.Label(self.frame, image=photo)
            background_label.image = photo
            background_label.place(relwidth=1, relheight=1)
        else:
            messagebox.showerror("Hata", "Arka plan resmi bulunamadı.")

        self.label_baslik = tk.Label(self.frame, text="Araç Kiralama Uygulamasına Hoşgeldiniz", font=("Helvetica", 20), fg="white", bg="black")
        self.label_baslik.pack(pady=20)

        self.label_kullanici_ad = tk.Label(self.frame, text="Kullanıcı Adı:", font=("Helvetica", 12), fg="white",
                                           bg="black")
        self.label_kullanici_ad.pack(pady=(0, 5))
        self.entry_kullanici_ad = tk.Entry(self.frame, font=("Helvetica", 12))
        self.entry_kullanici_ad.pack(pady=(0, 10), ipadx=5, ipady=5)

        self.label_sifre = tk.Label(self.frame, text="Şifre:", font=("Helvetica", 12), fg="white", bg="black")
        self.label_sifre.pack(pady=(0, 5))
        self.entry_sifre = tk.Entry(self.frame, show="*", font=("Helvetica", 12))
        self.entry_sifre.pack(pady=(0, 10), ipadx=5, ipady=5)

        self.button_giris = tk.Button(self.frame, text="Giriş Yap", command=self.giris_yap, font=("Helvetica", 12),
                                      bg="#3498DB", fg="white")
        self.button_giris.pack(pady=10)

        self.button_kayit = tk.Button(self.frame, text="Kayıt Ol", command=self.kayit_ol_ekranini_ac, font=("Helvetica", 12),
                                      bg="#E74C3C", fg="white")
        self.button_kayit.pack(pady=10)

    def giris_yap(self):
        kullanici_ad = self.entry_kullanici_ad.get()
        kullanici_sifre = self.entry_sifre.get()

        if not kullanici_ad or not kullanici_sifre:
            messagebox.showerror("Hata", "Lütfen Kullanıcı Adı ve Şifre Giriniz.")
            return

        try:
            self.cursor.execute(
                "SELECT id FROM kullanici_giris WHERE kullanici_ad = %s AND kullanici_sifre = %s",
                (kullanici_ad, kullanici_sifre))
            kullanici = self.cursor.fetchone()

            if kullanici:
                self.kullanici_id = kullanici[0]

                self.frame.destroy()
                self.arac_kiralama_sistemi()
            else:
                messagebox.showerror("Hata", "Kullanıcı adı veya şifre hatalı.")
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

    def kayit_ol_ekranini_ac(self):
        self.frame.destroy()

        self.frame_kayit = tk.Frame(self.root, bg="black", padx=20, pady=20)
        self.frame_kayit.pack(expand=True)

        self.label_bilgi_kayit = tk.Label(self.frame_kayit, text="Kullanıcı Adı ve Şifrenizi Belirleyin",
                                          font=("Helvetica", 14), fg="white", bg="black")
        self.label_bilgi_kayit.pack(pady=10)

        self.label_kullanici_ad_kayit = tk.Label(self.frame_kayit, text="Kullanıcı Adı:")
        self.label_kullanici_ad_kayit.pack(pady=(0, 5))
        self.entry_kullanici_ad_kayit = tk.Entry(self.frame_kayit)
        self.entry_kullanici_ad_kayit.pack(pady=(0, 10))

        self.label_sifre_kayit = tk.Label(self.frame_kayit, text="Şifre:")
        self.label_sifre_kayit.pack(pady=(0, 5))
        self.entry_sifre_kayit = tk.Entry(self.frame_kayit, show="*")
        self.entry_sifre_kayit.pack(pady=(0, 10))

        self.button_kayit = tk.Button(self.frame_kayit, text="Kayıt Ol", command=self.kayit_ol_gonder)
        self.button_kayit.pack(pady=10)

    def kayit_ol_gonder(self):
            kullanici_ad = self.entry_kullanici_ad_kayit.get()
            kullanici_sifre = self.entry_sifre_kayit.get()

            self.cursor.execute("SELECT COUNT(*) FROM kullanici_giris WHERE kullanici_ad = %s", (kullanici_ad,))
            kullanici_var_mi = self.cursor.fetchone()[0]

            if kullanici_var_mi == 0:
                self.cursor.execute("INSERT INTO kullanici_giris (kullanici_ad, kullanici_sifre) VALUES (%s, %s)",
                                    (kullanici_ad, kullanici_sifre))
                self.conn.commit()

                messagebox.showinfo("Başarılı", "Kullanıcı başarıyla oluşturuldu. Şimdi giriş yapabilirsiniz.")

                self.frame_kayit.destroy()
                self.giris_sayfasi()

            else:
                messagebox.showerror("Hata",
                                     "Bu kullanıcı adı zaten kullanılıyor. Lütfen farklı bir kullanıcı adı seçin.")
    def arac_kiralama_sistemi(self):
        self.frame_sag = tk.Frame(self.root, padx=20, pady=20, bg="black")
        self.frame_sag.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.label_secim = tk.Label(self.frame_sag,
                                    text="Kiralamak veya İade Etmek İstediğiniz Model ve Markayı Seçiniz",
                                    font=("Helvetica", 14), fg="white", bg="black")
        self.label_secim.pack(pady=10)

        self.label_marka = tk.Label(self.frame_sag, text="Marka:", fg="white", bg="black")
        self.label_marka.pack()
        self.entry_marka = tk.Entry(self.frame_sag)
        self.entry_marka.pack()

        self.label_model = tk.Label(self.frame_sag, text="Model:", fg="white", bg="black")
        self.label_model.pack()
        self.entry_model = tk.Entry(self.frame_sag)
        self.entry_model.pack()

        self.button_kirala = tk.Button(self.frame_sag, text="Araç Kirala", command=self.arac_kirala, bg="#3498DB", fg="white")
        self.button_kirala.pack(pady=10)

        self.button_iade = tk.Button(self.frame_sag, text="Araç İade Et", command=self.arac_iade, bg="#E74C3C", fg="white")
        self.button_iade.pack(pady=10)

        self.button_musait = tk.Button(self.frame_sag, text="Müsait Araç Listesi", command=self.musait_arac_listesi, bg="#2ECC71", fg="white")
        self.button_musait.pack(pady=10)

        self.button_gecmis = tk.Button(self.frame_sag, text="Kiralama Geçmişi", command=self.kiralama_gecmisi_goster,bg="#8E44AD", fg="white")
        self.button_gecmis.pack(pady=10)

    def arac_kirala(self):
        marka = self.entry_marka.get()
        model = self.entry_model.get()

        if self.kullanici_id is not None:
            self.cursor.execute(
                "SELECT arac_id, fiyat FROM araclar WHERE marka = %s AND model = %s AND durum = 'Müsait'",
                (marka, model))
            arac = self.cursor.fetchone()

            if arac:
                arac_id, fiyat = arac

                kira_tarihi = datetime.now().date()
                iade_tarihi = kira_tarihi + timedelta(days=random.randint(1, 7))

                self.cursor.execute(
                    "INSERT INTO kiralama_gecmisi (arac_id, kullanici_id, kira_tarihi, iade_tarihi, fiyat) VALUES (%s, %s, %s, %s, %s)",
                    (arac_id, self.kullanici_id, kira_tarihi, iade_tarihi, fiyat))

                self.cursor.execute("UPDATE araclar SET durum = 'Kiralandı' WHERE arac_id = %s", (arac_id,))
                self.conn.commit()

                messagebox.showinfo("Başarılı", "Araç başarıyla kiralandı. Ücret: {:.2f} TL".format(fiyat))
            else:
                messagebox.showerror("Hata", "Bu araç müsait değil veya bulunamadı.")
        else:
            messagebox.showerror("Hata", "Kullanıcı bulunamadı.")

    def arac_iade(self):
        marka = self.entry_marka.get()
        model = self.entry_model.get()

        if self.kullanici_id is not None:
            self.cursor.execute("SELECT arac_id FROM araclar WHERE marka = %s AND model = %s AND durum = 'Kiralandı'",
                                (marka, model))
            arac = self.cursor.fetchone()

            if arac:
                arac_id = arac[0]

                self.cursor.execute("UPDATE araclar SET durum = 'Müsait' WHERE arac_id = %s", (arac_id,))
                self.cursor.execute(
                    "UPDATE kiralama_gecmisi SET iade_tarihi = CURRENT_DATE WHERE arac_id = %s AND kullanici_id = %s",
                    (arac_id, self.kullanici_id))
                self.conn.commit()

                messagebox.showinfo("Başarılı", "Araç başarıyla iade edildi.")
            else:
                messagebox.showerror("Hata", "Araç bulunamadı veya kiralanmamış.")
        else:
            messagebox.showerror("Hata", "Kullanıcı bulunamadı.")

    def musait_arac_listesi(self):
        self.cursor.execute("SELECT marka, model FROM araclar WHERE durum = 'Müsait'")
        musait_araclar = self.cursor.fetchall()

        if musait_araclar:
            musait_arac_str = "\n".join([f"{marka} - {model}" for marka, model in musait_araclar])
            messagebox.showinfo("Müsait Araçlar", musait_arac_str)
        else:
            messagebox.showinfo("Müsait Araçlar", "Müsait araç bulunmamaktadır.")

    def kiralama_gecmisi_goster(self):
        if self.kullanici_id is None:
            messagebox.showerror("Hata", "Kullanıcı bulunamadı.")
            return

        self.guncelle_kiralama_gecmisi()

    def guncelle_kiralama_gecmisi(self):
        try:
            self.cursor.execute(
                "SELECT kullanici_ad FROM kullanici_giris WHERE id = %s",
                (self.kullanici_id,)
            )
            kullanici_ad = self.cursor.fetchone()[0]

            self.cursor.execute(
                "SELECT kiralama_gecmisi.*, araclar.marka, araclar.model, kiralama_gecmisi.kira_tarihi, kiralama_gecmisi.iade_tarihi FROM kiralama_gecmisi JOIN araclar ON kiralama_gecmisi.arac_id = araclar.arac_id WHERE kullanici_id = %s",
                (self.kullanici_id,)
            )
            kiralama_gecmisi = self.cursor.fetchall()

            if not kiralama_gecmisi:
                messagebox.showinfo("Bilgi", "Kiralama geçmişi bulunmamaktadır.")
                return

            gecmis_str = "\n".join(
                [f"{kullanici_ad} tarihinde {row[6]} - {row[7]} aracını kiraladı, {row[8]} tarihine kadar kullanıldı."
                 for row in
                 kiralama_gecmisi])

            if hasattr(self, "text_gecmis"):
                self.text_gecmis.destroy()

            self.text_gecmis = tk.Text(self.frame_sag, height=10, width=50, wrap=tk.WORD, fg="black", bg="white")
            self.text_gecmis.insert(tk.END, gecmis_str)
            self.text_gecmis.pack(pady=5)
        except Exception as e:
            messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    arac_kiralama_sistemi = AracKiralamaSistemi(root)
    root.mainloop()