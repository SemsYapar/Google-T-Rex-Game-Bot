from pyautogui import keyDown, keyUp, click
from PIL import ImageGrab, ImageOps
from time import sleep
from threading import Timer

class Dino_Bot:
	def __init__(self):
		self.RPL_BUTTON = [683, 390]#başlangıç butonunun kordinatları girilecek..
		self.DİNO_LAST_POİNT = [445, 395]#dinazorun en sağ ve en üst noktalarının(x ve y) kordinatlarını  alınız..
		"""NOT: RPL_BUTTON ve DİNO_LAST_POİNT dışındaki değerler kafadan atılmamış özenle seçilmiştir, memnun kalmassanız değiştiriniz..
		bu değerlerle 5000 yaptım şanslıysan sende yaparsın kodu anlıyana kadar aşağıdakilerle pek oynamamanı öneririm..:D"""

		self.x1_y1 = [50, 21]#bu ve alttaki değerler sizin yukarda belirlediğiniz dinazorun uç kordinatları toplanır,
		self.x2_y2 = [110, 30]#ve bu sayede dinazorunuzun gözü diyebileceğimiz dikdörten prizmamız oluşur.

		self.range = 17 #Dinazorun harita hızlandıkça haritaya ayak uydurmak için görüş mesafesinin artması gerek
		self.timer1 = Timer(20.0, self.stop)#ne kadar saniyede bir dinozorun görüş mesafesinin artıcağını belirler
		self.zipla = 0.06 #dinazor zıplaması gerektiğinde ne kadar süre space bassın(saniye cinsinden)

		self.stop_range = False#buna dokanma

	def restart_game(self):
		click(self.RPL_BUTTON)
		print("Bot Başlatılıyor..")

	def imgrabe_cactus(self):
		box = (self.DİNO_LAST_POİNT[0] + self.x1_y1[0] + self.now_range, self.DİNO_LAST_POİNT[1] + self.x1_y1[1],
		 self.DİNO_LAST_POİNT[0] + self.x2_y2[0] + self.now_range, self.DİNO_LAST_POİNT[1] + self.x2_y2[1]) 
		area = ImageGrab.grab(box)#burda yukarıda bahsettiğim değerlerle oluşturduğunuz karenin fotorafı çekilir.
		gray_area = ImageOps.grayscale(area)
		sum_area = sum(map(sum, gray_area.getcolors()))
		return sum_area#çekilen fotoraf fiks bir sayı değerine dönüştürülür ve değer olarak döndürülür.

	def need_jump(self):
		keyUp("down")	
		keyDown("space")
		sleep(self.zipla)
		keyUp("space")
		keyDown("down")

	def stop(self):
		self.stop_range = True

	def range_generator(self):
		self.now_range = 0
		while True:
			yield self.now_range 
			self.now_range += self.range 
			
	def main(self):
		range_list = self.range_generator()
		self.restart_game()
		while True:
			next(range_list)
			print(f"dinazorunun görüş menzili {self.now_range} arttı")
			dino_thread = Dino_Bot()#bu threading ıvır zıvırlarına takılma ben ekledim sayesinde zamanla dinazorun daha ileri bakıyor,
			dino_thread.timer1.start()#e ne işe yarıyor dersen şöyleki, oyun hızlandıkça fotorafı çekip tepki verme süremizi kısaltmaya yarıyor.
			keyDown("down")
			while True:
				if self.imgrabe_cactus() != 787:#yukarda döndürdüğümüz fonksiyon burda lazım oluyor işte,
					self.need_jump()#zıplaması gerekip gerekmediğini anlamak için normal değer olan 787 dışında her şeye duyarlıyız..
				if dino_thread.stop_range == True:#NOT eğer dinazorun görüş alanını değiştirdiyseniz "sum_area" fonksiyonunu print ile değerini bulup yukardaki if bloğuna bulduğunuz değeri yazın.
					break


if __name__ == "__main__":
	print("""Başlamak için Kordinatları doğru girdiğinizden ve arka planda oyunun replay düğmesinin gözüktüğünden emin olun..
(aksi halde bot başlayamaz.)\n
Ardından ""enter"" tuşu ile botu başlatabilirsiniz.\n""")
	input()
	dino_bot1 = Dino_Bot()
	dino_bot1.main()
		