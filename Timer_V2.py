import time
from threading import Timer
from tkinter import messagebox
from tkinter import *
from time import strftime
#Parameters tk window
entry1 = 0
root = Tk()
root.geometry('1110x500')
root.resizable(False, False)
root['bg'] = 'black'
root.title("--Boss timer--created by MrCronix--")
def start_timer():

	def tmbos1():
		h1 = int(entry_1.get())
		m1 = int(entry_2.get())
		s1 = int(entry_3.get())
		sec1 = int((h1*60*60)+(m1*60)+s1)
		def tmbosready1():
			lbtime1.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Древній лучник (1) 15lvl PvP:OFF\nРівні рун: Звичайні: 1. Легендарні: 0.\nОсобливі руни: всі руни які немають рівнів")
		t1 = Timer(sec1, tmbosready1)
		t1.start()
		lbtime1.config(bg="green")
	def tmbos2():
		h2 = int(entry_4.get())
		m2 = int(entry_5.get())
		s2 = int(entry_6.get())
		sec2 = int((h2*60*60)+(m2*60)+s2)
		def tmbosready2():
			lbtime2.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Слизень (2) 20lvl PvP:OFF\nРівні рун: Звичайні: 1. Легендарні: 0.\nОсобливі руни: всі руни які немають рівнів")
		t2 = Timer(sec2, tmbosready2)
		t2.start()
		lbtime2.config(bg="green")
	def tmbos3():
		h3 = int(entry_7.get())
		m3 = int(entry_8.get())
		s3 = int(entry_9.get())
		sec3 = int((h3*60*60)+(m3*60)+s3)
		def tmbosready3():
			lbtime3.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Страж (3) 25lvl PvP:OFF\nРівні рун: Звичайні: 1. Легендарні: 1.\nОсобливі руни: всі руни які немають рівнів")
		t3 = Timer(sec3, tmbosready3)
		t3.start()
		lbtime3.config(bg="green")
	def tmbos4():
		h4 = int(entry_10.get())
		m4 = int(entry_11.get())
		s4 = int(entry_12.get())
		sec4 = int((h4*60*60)+(m4*60)+s4)
		def tmbosready4():
			lbtime4.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Близнеці (4) 35lvl PvP:OFF\nРівні рун: Звичайні: 1. Легендарні: 1.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t4 = Timer(sec4, tmbosready4)
		t4.start()
		lbtime4.config(bg="green")
	def tmbos5():
		h5 = int(entry_13.get())
		m5 = int(entry_14.get())
		s5 = int(entry_15.get())
		sec5 = int((h5*60*60)+(m5*60)+s5)
		def tmbosready5():
			lbtime5.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Повелитель вогню (5) 40lvl PvP:OFF\nРівні рун: Звичайні: 1. Легендарні: 1.\nОсобливі руни: Немає")
		t5 = Timer(sec5, tmbosready5)
		t5.start()
		lbtime5.config(bg="green")
	def tmbos6():
		h6 = int(entry_16.get())
		m6 = int(entry_17.get())
		s6 = int(entry_18.get())
		sec6 = int((h6*60*60)+(m6*60)+s6)
		def tmbosready6():
			lbtime6.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Павучиха (6) 45lvl PvP:OFF\nРівні рун: Звичайні: 2. Легендарні: 1.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t6 = Timer(sec6, tmbosready6)
		t6.start()
		lbtime6.config(bg="green")
	def tmbos7():
		h7 = int(entry_19.get())
		m7 = int(entry_20.get())
		s7 = int(entry_21.get())
		sec7 = int((h7*60*60)+(m7*60)+s7)
		def tmbosready7():
			lbtime7.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Утопленик (7) 50lvl PvP:ON\nРівні рун: Звичайні: 2. Легендарні: 1.\nОсобливі руни: Немає")
		t7 = Timer(sec7, tmbosready7)
		t7.start()
		lbtime7.config(bg="green")
	def tmbos8():
		h8 = int(entry_22.get())
		m8 = int(entry_23.get())
		s8 = int(entry_24.get())
		sec8 = int((h8*60*60)+(m8*60)+s8)
		def tmbosready8():
			lbtime8.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Колдун (8) 55lvl PvP:OFF\nРівні рун: Звичайні: 2. Легендарні: 1.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t8 = Timer(sec8, tmbosready8)
		t8.start()
		lbtime8.config(bg="green")
	def tmbos9():
		h9 = int(entry_25.get())
		m9 = int(entry_26.get())
		s9 = int(entry_27.get())
		sec9 = int((h9*60*60)+(m9*60)+s9)
		def tmbosready9():
			lbtime9.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Чорна смерть (9) 60lvl PvP:ON\nРівні рун: Звичайні: 2. Легендарні: 2.\nОсобливі руни: Немає")
		t9 = Timer(sec9, tmbosready9)
		t9.start()
		lbtime9.config(bg="green")
	def tmbos10():
		h10 = int(entry_28.get())
		m10 = int(entry_29.get())
		s10 = int(entry_30.get())
		sec10 = int((h10*60*60)+(m10*60)+s10)
		def tmbosready10():
			lbtime10.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Наїздник (10) 65lvl PvP:OFF\nРівні рун: Звичайні: 2. Легендарні: 2.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t10 = Timer(sec10, tmbosready10)
		t10.start()
		lbtime10.config(bg="green")
	def tmbos11():
		h11 = int(entry_31.get())
		m11 = int(entry_32.get())
		s11 = int(entry_33.get())
		sec11 = int((h11*60*60)+(m11*60)+s11)
		def tmbosready11():
			lbtime11.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Розбійник (11) 70lvl PvP:ON\nРівні рун: Звичайні: 2. Легендарні: 2.\nОсобливі руни: Немає")
		t11 = Timer(sec11, tmbosready11)
		t11.start()
		lbtime11.config(bg="green")
	def tmbos12():
		h12 = int(entry_34.get())
		m12 = int(entry_35.get())
		s12 = int(entry_36.get())
		sec12 = int((h12*60*60)+(m12*60)+s12)
		def tmbosready12():
			lbtime12.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Лавовий Куб (12) 75lvl PvP:OFF\nРівні рун: Звичайні: 2. Легендарні: 2.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t12 = Timer(sec12, tmbosready12)
		t12.start()
		lbtime12.config(bg="green")
	def tmbos13():
		h13 = int(entry_37.get())
		m13 = int(entry_38.get())
		s13 = int(entry_39.get())
		sec13 = int((h13*60*60)+(m13*60)+s13)
		def tmbosready13():
			lbtime13.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Призрачний охотник (13) 80lvl PvP:ON\nРівні рун: Звичайні: 2. Легендарні: 2.\nОсобливі руни: Немає")
		t13 = Timer(sec13, tmbosready13)
		t13.start()
		lbtime13.config(bg="green")
	def tmbos14():
		h14 = int(entry_40.get())
		m14 = int(entry_41.get())
		s14 = int(entry_42.get())
		sec14 = int((h14*60*60)+(m14*60)+s14)
		def tmbosready14():
			lbtime14.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Чорний дракон (14) 85lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Чешуя дракона I, II, III.\nРЕЙДОВИЙ (РКР)")
		t14 = Timer(sec14, tmbosready14)
		t14.start()
		lbtime14.config(bg="green")
	def tmbos15():
		h15 = int(entry_43.get())
		m15 = int(entry_44.get())
		s15 = int(entry_45.get())
		sec15 = int((h15*60*60)+(m15*60)+s15)
		def tmbosready15():
			lbtime15.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Гігант (15) 90lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Немає")
		t15 = Timer(sec15, tmbosready15)
		t15.start()
		lbtime15.config(bg="green")
	def tmbos16():
		h16 = int(entry_46.get())
		m16 = int(entry_47.get())
		s16 = int(entry_48.get())
		sec16 = int((h16*60*60)+(m16*60)+s16)
		def tmbosready16():
			lbtime16.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Проклятий легіон (16) 95lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t16 = Timer(sec16, tmbosready16)
		t16.start()
		lbtime16.config(bg="green")
	def tmbos17():
		h17 = int(entry_49.get())
		m17 = int(entry_50.get())
		s17 = int(entry_51.get())
		sec17 = int((h17*60*60)+(m17*60)+s17)
		def tmbosready17():
			lbtime17.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Монстр (17) 100lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Монстр II, III.")
		t17 = Timer(sec17, tmbosready17)
		t17.start()
		lbtime17.config(bg="green")
	def tmbos18():
		h18 = int(entry_52.get())
		m18 = int(entry_53.get())
		s18 = int(entry_54.get())
		sec18 = int((h18*60*60)+(m18*60)+s18)
		def tmbosready18():
			lbtime18.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Некромант (18) 105lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t18 = Timer(sec18, tmbosready18)
		t18.start()
		lbtime18.config(bg="green")
	def tmbos19():
		h19 = int(entry_55.get())
		m19 = int(entry_56.get())
		s19 = int(entry_57.get())
		sec19 = int((h19*60*60)+(m19*60)+s19)
		def tmbosready19():
			lbtime19.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Пожератель тьми (19) 110lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Немає")
		t19 = Timer(sec19, tmbosready19)
		t19.start()
		lbtime19.config(bg="green")
	def tmbos20():
		h20 = int(entry_58.get())
		m20 = int(entry_59.get())
		s20 = int(entry_60.get())
		sec20 = int((h20*60*60)+(m20*60)+s20)
		def tmbosready20():
			lbtime20.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Чудовисько (20) 115lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 2.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t20 = Timer(sec20, tmbosready20)
		t20.start()
		lbtime20.config(bg="green")
	def tmbos21():
		h21 = int(entry_61.get())
		m21 = int(entry_62.get())
		s21 = int(entry_63.get())
		sec21 = int((h21*60*60)+(m21*60)+s21)
		def tmbosready21():
			lbtime21.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Кузнець (21) 120lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t21 = Timer(sec21, tmbosready21)
		t21.start()
		lbtime21.config(bg="green")
	def tmbos22():
		h22 = int(entry_64.get())
		m22 = int(entry_65.get())
		s22 = int(entry_66.get())
		sec22 = int((h22*60*60)+(m22*60)+s22)
		def tmbosready22():
			lbtime22.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Могутній шалкер (22) 125lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t22 = Timer(sec22, tmbosready22)
		t22.start()
		lbtime22.config(bg="green")
	def tmbos23():
		h23 = int(entry_67.get())
		m23 = int(entry_68.get())
		s23 = int(entry_69.get())
		sec23 = int((h23*60*60)+(m23*60)+s23)
		def tmbosready23():
			lbtime23.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Заклинатель (23) 130lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t23 = Timer(sec23, tmbosready23)
		t23.start()
		lbtime23.config(bg="green")
	def tmbos24():
		h24 = int(entry_70.get())
		m24 = int(entry_71.get())
		s24 = int(entry_72.get())
		sec24 = int((h24*60*60)+(m24*60)+s24)
		def tmbosready24():
			lbtime24.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Мертний всадник (24) 140lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t24 = Timer(sec24, tmbosready24)
		t24.start()
		lbtime24.config(bg="green")
	def tmbos25():
		h25 = int(entry_73.get())
		m25 = int(entry_74.get())
		s25 = int(entry_75.get())
		sec25 = int((h25*60*60)+(m25*60)+s25)
		def tmbosready25():
			lbtime25.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Самурай (25) 150lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t25 = Timer(sec25, tmbosready25)
		t25.start()
		lbtime25.config(bg="green")
	def tmbos26():
		h26 = int(entry_76.get())
		m26 = int(entry_77.get())
		s26 = int(entry_78.get())
		sec26 = int((h26*60*60)+(m26*60)+s26)
		def tmbosready26():
			lbtime26.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Повелитель мертвих (26) 155lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР)")
		t26 = Timer(sec26, tmbosready26)
		t26.start()
		lbtime26.config(bg="green")
	def tmbos27():
		h27 = int(entry_79.get())
		m27 = int(entry_80.get())
		s27 = int(entry_81.get())
		sec27 = int((h27*60*60)+(m27*60)+s27)
		def tmbosready27():
			lbtime27.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Тіньовий лорд (27) 160lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t27 = Timer(sec27, tmbosready27)
		t27.start()
		lbtime27.config(bg="green")
	def tmbos28():
		h28 = int(entry_82.get())
		m28 = int(entry_83.get())
		s28 = int(entry_84.get())
		sec28 = int((h28*60*60)+(m28*60)+s28)
		def tmbosready28():
			lbtime28.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Голіаф (28) 180lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t28 = Timer(sec28, tmbosready28)
		t28.start()
		lbtime28.config(bg="green")
	def tmbos29():
		h29 = int(entry_85.get())
		m29 = int(entry_86.get())
		s29 = int(entry_87.get())
		sec29 = int((h29*60*60)+(m29*60)+s29)
		def tmbosready29():
			lbtime29.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Винищувач (29) 185lvl PvP:OFF\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає\nРЕЙДОВИЙ (РКР")
		t29 = Timer(sec29, tmbosready29)
		t29.start()
		lbtime29.config(bg="green")
	def tmbos30():
		h30 = int(entry_88.get())
		m30 = int(entry_89.get())
		s30 = int(entry_90.get())
		sec30 = int((h30*60*60)+(m30*60)+s30)
		def tmbosready30():
			lbtime30.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Крик (30) 200lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t30 = Timer(sec30, tmbosready30)
		t30.start()
		lbtime30.config(bg="green")
	def tmbos31():
		h31 = int(entry_91.get())
		m31 = int(entry_92.get())
		s31 = int(entry_93.get())
		sec31 = int((h31*60*60)+(m31*60)+s31)
		def tmbosready31():
			lbtime31.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Спектральний куб (31) 220lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t31 = Timer(sec31, tmbosready31)
		t31.start()
		lbtime31.config(bg="green")
	def tmbos32():
		h32 = int(entry_94.get())
		m32 = int(entry_95.get())
		s32 = int(entry_96.get())
		sec32 = int((h32*60*60)+(m32*60)+s32)
		def tmbosready32():
			lbtime32.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Тінь (32) 230lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t32 = Timer(sec32, tmbosready32)
		t32.start()
		lbtime32.config(bg="green")
	def tmbos33():
		h33 = int(entry_97.get())
		m33 = int(entry_98.get())
		s33 = int(entry_99.get())
		sec33 = int((h33*60*60)+(m33*60)+s33)
		def tmbosready33():
			lbtime33.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Вістник аду (33) 250lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t33 = Timer(sec33, tmbosready33)
		t33.start()
		lbtime33.config(bg="green")
	def tmbos34():
		h34 = int(entry_100.get())
		m34 = int(entry_101.get())
		s34 = int(entry_102.get())
		sec34 = int((h34*60*60)+(m34*60)+s34)
		def tmbosready34():
			lbtime34.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Іфріть (34) 280lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t34 = Timer(sec34, tmbosready34)
		t34.start()
		lbtime34.config(bg="green")
	def tmbos35():
		h35 = int(entry_103.get())
		m35 = int(entry_104.get())
		s35 = int(entry_105.get())
		sec35 = int((h35*60*60)+(m35*60)+s35)
		def tmbosready35():
			lbtime35.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Піглін (35) 290lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t35 = Timer(sec35, tmbosready35)
		t35.start()
		lbtime35.config(bg="green")
	def tmbos36():
		h36 = int(entry_106.get())
		m36 = int(entry_107.get())
		s36 = int(entry_108.get())
		sec36 = int((h36*60*60)+(m36*60)+s36)
		def tmbosready36():
			lbtime36.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Хоглін (36) 300lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t36 = Timer(sec36, tmbosready36)
		t36.start()
		lbtime36.config(bg="green")
	def tmbos37():
		h37 = int(entry_109.get())
		m37 = int(entry_110.get())
		s37 = int(entry_111.get())
		sec37 = int((h37*60*60)+(m37*60)+s37)
		def tmbosready37():
			lbtime37.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Зомбі піглін (37) 310lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t37 = Timer(sec37, tmbosready37)
		t37.start()
		lbtime37.config(bg="green")
	def tmbos38():
		h38 = int(entry_112.get())
		m38 = int(entry_113.get())
		s38 = int(entry_114.get())
		sec38 = int((h38*60*60)+(m38*60)+s38)
		def tmbosready38():
			lbtime38.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Брутальний піглін (38) 320lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t38 = Timer(sec38, tmbosready38)
		t38.start()
		lbtime38.config(bg="green")
	def tmbos39():
		h39 = int(entry_115.get())
		m39 = int(entry_116.get())
		s39 = int(entry_117.get())
		sec39 = int((h39*60*60)+(m39*60)+s39)
		def tmbosready39():
			lbtime39.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Магма (39) 330lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t39 = Timer(sec39, tmbosready39)
		t39.start()
		lbtime39.config(bg="green")
	def tmbos40():
		h40 = int(entry_118.get())
		m40 = int(entry_119.get())
		s40 = int(entry_120.get())
		sec40 = int((h40*60*60)+(m40*60)+s40)
		def tmbosready40():
			lbtime40.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Зоглін (40) 340lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t40 = Timer(sec40, tmbosready40)
		t40.start()
		lbtime40.config(bg="green")
	def tmbos41():
		h41 = int(entry_121.get())
		m41 = int(entry_122.get())
		s41 = int(entry_123.get())
		sec41 = int((h41*60*60)+(m41*60)+s41)
		def tmbosready41():
			lbtime41.config(bg="red")
			messagebox.showinfo(title="Boss has spawned",message="Адський рицарь (41) 350lvl PvP:ON\nРівні рун: Звичайні: 3. Легендарні: 3.\nОсобливі руни: Немає")
		t41 = Timer(sec41, tmbosready41)
		t41.start()
		lbtime41.config(bg="green")
	def custime():
		h42 = int(entry_124.get())
		m42 = int(entry_125.get())
		s42 = int(entry_126.get())
		sec42 = int((h42*60*60)+(m42*60)+s42)
		def custimeready():
			lbtime42.config(bg="red")
			messagebox.showinfo(title="Your timer",message="{}".format(entry_custom.get()))
		t42 = Timer(sec42, custimeready)
		t42.start()
		lbtime42.config(bg="green")

	#Labels create and place
	labels_names_list_1 = ["Древній лучник", "Слизень", "Страж", "Близнеці", "Повелитель вогню", "Павучиха", "Утопленик", "Колдун", "Чорна смерть", "Наїздник", "Розбійник", "Лавовий Куб", "Призрачний охотник", "Чорний дракон"]
	labels_names_list_2 = ["Гігант", "Проклятий Легіон", "Монстр", "Некромант", "Пожератель тьми", "Чудовисько", "Кузнець", "Могутній шалкер", "Заклинатель", "Мертний всадник", "Самурай", "Повелитель мертвих", "Тіньовий лорд", "Голіаф"]
	labels_names_list_3 = ["Винищувач", "Крик", "Спектральний куб", "Тінь", "Вістник аду", "Іфріть", "Піглін", "Хоглін", "Зомбі піглін", "Брутальний піглін", "Магма", "Зоглін", "Адський рицарь"]
	a=5
	b=0
	for labels in labels_names_list_1:
		Label(root, text="{}".format(labels_names_list_1[b]),font=16,bg="black",fg="white").place(x=0,y=a)
		a+=35 
		b+=1
	a=5
	b=0
	for labels in labels_names_list_2:
		Label(root, text="{}".format(labels_names_list_2[b]),font=16,bg="black",fg="white").place(x=370,y=a)
		a+=35
		b+=1
	a=5
	b=0
	for labels in labels_names_list_3:
		Label(root, text="{}".format(labels_names_list_3[b]),font=16,bg="black",fg="white").place(x=740,y=a)
		a+=35
		b+=1
	entry_custom = Entry(font=16,width=15)
	entry_custom.place(x=740,y=460)
	#Entrys create
	entry_1 = Entry(font=16,width=3)
	entry_2 = Entry(font=16,width=3)
	entry_3 = Entry(font=16,width=3)
	entry_4 = Entry(font=16,width=3)
	entry_5 = Entry(font=16,width=3)
	entry_6 = Entry(font=16,width=3)
	entry_7 = Entry(font=16,width=3)
	entry_8 = Entry(font=16,width=3)
	entry_9 = Entry(font=16,width=3)
	entry_10 = Entry(font=16,width=3)
	entry_11 = Entry(font=16,width=3)
	entry_12 = Entry(font=16,width=3)
	entry_13 = Entry(font=16,width=3)
	entry_14 = Entry(font=16,width=3)
	entry_15 = Entry(font=16,width=3)
	entry_16 = Entry(font=16,width=3)
	entry_17 = Entry(font=16,width=3)
	entry_18 = Entry(font=16,width=3)
	entry_19 = Entry(font=16,width=3)
	entry_20 = Entry(font=16,width=3)
	entry_21 = Entry(font=16,width=3)
	entry_22 = Entry(font=16,width=3)
	entry_23 = Entry(font=16,width=3)
	entry_24 = Entry(font=16,width=3)
	entry_25 = Entry(font=16,width=3)
	entry_26 = Entry(font=16,width=3)
	entry_27 = Entry(font=16,width=3)
	entry_28 = Entry(font=16,width=3)
	entry_29 = Entry(font=16,width=3)
	entry_30 = Entry(font=16,width=3)
	entry_31 = Entry(font=16,width=3)
	entry_32 = Entry(font=16,width=3)
	entry_33 = Entry(font=16,width=3)
	entry_34 = Entry(font=16,width=3)
	entry_35 = Entry(font=16,width=3)
	entry_36 = Entry(font=16,width=3)
	entry_37 = Entry(font=16,width=3)
	entry_38 = Entry(font=16,width=3)
	entry_39 = Entry(font=16,width=3)
	entry_40 = Entry(font=16,width=3)
	entry_41 = Entry(font=16,width=3)
	entry_42 = Entry(font=16,width=3)
	entry_43 = Entry(font=16,width=3)
	entry_44 = Entry(font=16,width=3)
	entry_45 = Entry(font=16,width=3)
	entry_46 = Entry(font=16,width=3)
	entry_47 = Entry(font=16,width=3)
	entry_48 = Entry(font=16,width=3)
	entry_49 = Entry(font=16,width=3)
	entry_50 = Entry(font=16,width=3)
	entry_51 = Entry(font=16,width=3)
	entry_52 = Entry(font=16,width=3)
	entry_53 = Entry(font=16,width=3)
	entry_54 = Entry(font=16,width=3)
	entry_55 = Entry(font=16,width=3)
	entry_56 = Entry(font=16,width=3)
	entry_57 = Entry(font=16,width=3)
	entry_58 = Entry(font=16,width=3)
	entry_59 = Entry(font=16,width=3)
	entry_60 = Entry(font=16,width=3)
	entry_61 = Entry(font=16,width=3)
	entry_62 = Entry(font=16,width=3)
	entry_63 = Entry(font=16,width=3)
	entry_64 = Entry(font=16,width=3)
	entry_65 = Entry(font=16,width=3)
	entry_66 = Entry(font=16,width=3)
	entry_67 = Entry(font=16,width=3)
	entry_68 = Entry(font=16,width=3)
	entry_69 = Entry(font=16,width=3)
	entry_70 = Entry(font=16,width=3)
	entry_71 = Entry(font=16,width=3)
	entry_72 = Entry(font=16,width=3)
	entry_73 = Entry(font=16,width=3)
	entry_74 = Entry(font=16,width=3)
	entry_75 = Entry(font=16,width=3)
	entry_76 = Entry(font=16,width=3)
	entry_77 = Entry(font=16,width=3)
	entry_78 = Entry(font=16,width=3)
	entry_79 = Entry(font=16,width=3)
	entry_80 = Entry(font=16,width=3)
	entry_81 = Entry(font=16,width=3)
	entry_82 = Entry(font=16,width=3)
	entry_83 = Entry(font=16,width=3)
	entry_84 = Entry(font=16,width=3)
	entry_85 = Entry(font=16,width=3)
	entry_86 = Entry(font=16,width=3)
	entry_87 = Entry(font=16,width=3)
	entry_88 = Entry(font=16,width=3)
	entry_89 = Entry(font=16,width=3)
	entry_90 = Entry(font=16,width=3)
	entry_91 = Entry(font=16,width=3)
	entry_92 = Entry(font=16,width=3)
	entry_93 = Entry(font=16,width=3)
	entry_94 = Entry(font=16,width=3)
	entry_95 = Entry(font=16,width=3)
	entry_96 = Entry(font=16,width=3)
	entry_97 = Entry(font=16,width=3)
	entry_98 = Entry(font=16,width=3)
	entry_99 = Entry(font=16,width=3)
	entry_100 = Entry(font=16,width=3)
	entry_101 = Entry(font=16,width=3)
	entry_102 = Entry(font=16,width=3)
	entry_103 = Entry(font=16,width=3)
	entry_104 = Entry(font=16,width=3)
	entry_105 = Entry(font=16,width=3)
	entry_106 = Entry(font=16,width=3)
	entry_107 = Entry(font=16,width=3)
	entry_108 = Entry(font=16,width=3)
	entry_109 = Entry(font=16,width=3)
	entry_110 = Entry(font=16,width=3)
	entry_111 = Entry(font=16,width=3)
	entry_112 = Entry(font=16,width=3)
	entry_113 = Entry(font=16,width=3)
	entry_114 = Entry(font=16,width=3)
	entry_115 = Entry(font=16,width=3)
	entry_116 = Entry(font=16,width=3)
	entry_117 = Entry(font=16,width=3)
	entry_118 = Entry(font=16,width=3)
	entry_119 = Entry(font=16,width=3)
	entry_120 = Entry(font=16,width=3)
	entry_121 = Entry(font=16,width=3)
	entry_122 = Entry(font=16,width=3)
	entry_123 = Entry(font=16,width=3)
	entry_124 = Entry(font=16,width=3)
	entry_125 = Entry(font=16,width=3)
	entry_126 = Entry(font=16,width=3)

	#placed entrys and set "0" in line
	ena=5
	entrys_list = [entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_7, entry_8, entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15, entry_16, entry_17, entry_18, entry_19, entry_20, entry_21, entry_22, entry_23, entry_24, entry_25, entry_26, entry_27, entry_28, entry_29, entry_30, entry_31, entry_32, entry_33, entry_34, entry_35, entry_36, entry_37, entry_38, entry_39, entry_40, entry_41, entry_42, entry_43, entry_44, entry_45, entry_46, entry_47, entry_48, entry_49, entry_50, entry_51, entry_52, entry_53, entry_54, entry_55, entry_56, entry_57, entry_58, entry_59, entry_60, entry_61, entry_62, entry_63, entry_64, entry_65, entry_66, entry_67, entry_68, entry_69, entry_70, entry_71, entry_72, entry_73, entry_74, entry_75, entry_76, entry_77, entry_78, entry_79, entry_80, entry_81, entry_82, entry_83, entry_84, entry_85, entry_86, entry_87, entry_88, entry_89, entry_90, entry_91, entry_92, entry_93, entry_94, entry_95, entry_96, entry_97, entry_98, entry_99, entry_100, entry_101, entry_102, entry_103, entry_104, entry_105, entry_106, entry_107, entry_108, entry_109, entry_110, entry_111, entry_112, entry_113, entry_114, entry_115, entry_116, entry_117, entry_118, entry_119, entry_120, entry_121, entry_122, entry_123, entry_124, entry_125, entry_126]
	for i in range(0, 42, 3):
		entrys_list[i].place(x=160,y=ena)
		entrys_list[i+1].place(x=200,y=ena)
		entrys_list[i+2].place(x=240,y=ena)
		ena+=35
	ena=5
	for i in range(42, 84, 3):
		entrys_list[i].place(x=530,y=ena)
		entrys_list[i+1].place(x=570,y=ena)
		entrys_list[i+2].place(x=610,y=ena)
		ena+=35
	ena=5
	for i in range(84, 126, 3):
		entrys_list[i].place(x=900,y=ena)
		entrys_list[i+1].place(x=940,y=ena)
		entrys_list[i+2].place(x=980,y=ena)
		ena+=35
	for i in entrys_list:
		i.insert(0,"0")

	#Labels what showing the time
	lbtime1 = Label(text="V",font=16,bg="red")
	lbtime2 = Label(text="V",font=16,bg="red")
	lbtime3 = Label(text="V",font=16,bg="red")
	lbtime4 = Label(text="V",font=16,bg="red")
	lbtime5 = Label(text="V",font=16,bg="red")
	lbtime6 = Label(text="V",font=16,bg="red")
	lbtime7 = Label(text="V",font=16,bg="red")
	lbtime8 = Label(text="V",font=16,bg="red")
	lbtime9 = Label(text="V",font=16,bg="red")
	lbtime10 = Label(text="V",font=16,bg="red")
	lbtime11 = Label(text="V",font=16,bg="red")
	lbtime12 = Label(text="V",font=16,bg="red")
	lbtime13 = Label(text="V",font=16,bg="red")
	lbtime14 = Label(text="V",font=16,bg="red")
	lbtime15 = Label(text="V",font=16,bg="red")
	lbtime16 = Label(text="V",font=16,bg="red")
	lbtime17 = Label(text="V",font=16,bg="red")
	lbtime18 = Label(text="V",font=16,bg="red")
	lbtime19 = Label(text="V",font=16,bg="red")
	lbtime20 = Label(text="V",font=16,bg="red")
	lbtime21 = Label(text="V",font=16,bg="red")
	lbtime22 = Label(text="V",font=16,bg="red")
	lbtime23 = Label(text="V",font=16,bg="red")
	lbtime24 = Label(text="V",font=16,bg="red")
	lbtime25 = Label(text="V",font=16,bg="red")
	lbtime26 = Label(text="V",font=16,bg="red")
	lbtime27 = Label(text="V",font=16,bg="red")
	lbtime28 = Label(text="V",font=16,bg="red")
	lbtime29 = Label(text="V",font=16,bg="red")
	lbtime30 = Label(text="V",font=16,bg="red")
	lbtime31 = Label(text="V",font=16,bg="red")
	lbtime32 = Label(text="V",font=16,bg="red")
	lbtime33 = Label(text="V",font=16,bg="red")
	lbtime34 = Label(text="V",font=16,bg="red")
	lbtime35 = Label(text="V",font=16,bg="red")
	lbtime36 = Label(text="V",font=16,bg="red")
	lbtime37 = Label(text="V",font=16,bg="red")
	lbtime38 = Label(text="V",font=16,bg="red")
	lbtime39 = Label(text="V",font=16,bg="red")
	lbtime40 = Label(text="V",font=16,bg="red")
	lbtime41 = Label(text="V",font=16,bg="red")
	lbtime42 = Label(text="V",font=16,bg="red")
	lb_list_1 = [lbtime1, lbtime2, lbtime3, lbtime4, lbtime5, lbtime6, lbtime7, lbtime8, lbtime9, lbtime10, lbtime11, lbtime12, lbtime13, lbtime14]
	lb_list_2 = [lbtime15, lbtime16, lbtime17, lbtime18, lbtime19, lbtime20, lbtime21, lbtime22, lbtime23, lbtime24, lbtime25, lbtime26, lbtime27, lbtime28]
	lb_list_3 = [lbtime29, lbtime30, lbtime31, lbtime32, lbtime33, lbtime34, lbtime35, lbtime36, lbtime37, lbtime38, lbtime39, lbtime40, lbtime41, lbtime42]
	lbt = 5
	for i in lb_list_1:
		i.place(x=340,y=lbt)
		lbt+=35
	lbt = 5
	for i in lb_list_2:
		i.place(x=710,y=lbt)
		lbt+=35
	lbt = 5
	for i in lb_list_3:
		i.place(x=1080,y=lbt)
		lbt+=35

	class All_timers():
		def __init__(self, ms, lb, entry1, entry2, entry3): #all_timers("fdgdg", lbtime1, entry_1, entry_2, entry_3)
			self.entry1 = entry1
			self.entry2 = entry2
			self.entry3 = entry3
			self.ms = ms
			self.h = int(entry1.get())
			print(self.h)
			self.m = int(entry2.get())
			print(self.m)
			self.s = int(entry3.get())
			print(self.s)
			self.sec = int((self.h*60*60)+(self.m*60)+self.s)
			print(self.sec)
			def tmbosready():
				#lb.config(bg="red")
				messagebox.showinfo(title="Boss has spawned",message=self.ms)
			t = Timer(self.sec, tmbosready)
			t.start()
			#lb.config(bg="green")

	#Buttons
	Button(text="start",font=16,height=1,command=All_timers("fdgdg", 1, entry_1, entry_2, entry_3)).place(x=280,y=5)
	Button(text="start",font=16,height=1,command=tmbos2).place(x=280,y=40)
	Button(text="start",font=16,height=1,command=tmbos3).place(x=280,y=75)
	Button(text="start",font=16,height=1,command=tmbos4).place(x=280,y=110)
	Button(text="start",font=16,height=1,command=tmbos5).place(x=280,y=145)
	Button(text="start",font=16,height=1,command=tmbos6).place(x=280,y=180)
	Button(text="start",font=16,height=1,command=tmbos7).place(x=280,y=215)
	Button(text="start",font=16,height=1,command=tmbos8).place(x=280,y=250)
	Button(text="start",font=16,height=1,command=tmbos9).place(x=280,y=285)
	Button(text="start",font=16,height=1,command=tmbos10).place(x=280,y=320)
	Button(text="start",font=16,height=1,command=tmbos11).place(x=280,y=355)
	Button(text="start",font=16,height=1,command=tmbos12).place(x=280,y=390)
	Button(text="start",font=16,height=1,command=tmbos13).place(x=280,y=425)
	Button(text="start",font=16,height=1,command=tmbos14).place(x=280,y=460)
	#Buttons
	Button(text="start",font=16,height=1,command=tmbos15).place(x=650,y=5)
	Button(text="start",font=16,height=1,command=tmbos16).place(x=650,y=40)
	Button(text="start",font=16,height=1,command=tmbos17).place(x=650,y=75)
	Button(text="start",font=16,height=1,command=tmbos18).place(x=650,y=110)
	Button(text="start",font=16,height=1,command=tmbos19).place(x=650,y=145)
	Button(text="start",font=16,height=1,command=tmbos20).place(x=650,y=180)
	Button(text="start",font=16,height=1,command=tmbos21).place(x=650,y=215)
	Button(text="start",font=16,height=1,command=tmbos22).place(x=650,y=250)
	Button(text="start",font=16,height=1,command=tmbos23).place(x=650,y=285)
	Button(text="start",font=16,height=1,command=tmbos24).place(x=650,y=320)
	Button(text="start",font=16,height=1,command=tmbos25).place(x=650,y=355)
	Button(text="start",font=16,height=1,command=tmbos26).place(x=650,y=390)
	Button(text="start",font=16,height=1,command=tmbos27).place(x=650,y=425)
	Button(text="start",font=16,height=1,command=tmbos28).place(x=650,y=460)
	#Buttons
	Button(text="start",font=16,height=1,command=tmbos29).place(x=1020,y=5)
	Button(text="start",font=16,height=1,command=tmbos30).place(x=1020,y=40)
	Button(text="start",font=16,height=1,command=tmbos31).place(x=1020,y=75)
	Button(text="start",font=16,height=1,command=tmbos32).place(x=1020,y=110)
	Button(text="start",font=16,height=1,command=tmbos33).place(x=1020,y=145)
	Button(text="start",font=16,height=1,command=tmbos34).place(x=1020,y=180)
	Button(text="start",font=16,height=1,command=tmbos35).place(x=1020,y=215)
	Button(text="start",font=16,height=1,command=tmbos36).place(x=1020,y=250)
	Button(text="start",font=16,height=1,command=tmbos37).place(x=1020,y=285)
	Button(text="start",font=16,height=1,command=tmbos38).place(x=1020,y=320)
	Button(text="start",font=16,height=1,command=tmbos39).place(x=1020,y=355)
	Button(text="start",font=16,height=1,command=tmbos40).place(x=1020,y=390)
	Button(text="start",font=16,height=1,command=tmbos41).place(x=1020,y=425)
	Button(text="start",font=16,height=1,command=custime).place(x=1020,y=460)

if __name__ == '__main__':
	start_timer()

root.mainloop()