from tkinter import *
import math , random , os
from tkinter import messagebox
class Super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super-Market: سوبر ماركت')
        self.root.resizable(False,False)
        #self.root.iconbitmap('D:\\icone.ico')
        title = Label(self.root , text='ادارة المشاريع : سوبر ماركت',fg='white',bg='#0B2F3A',font=('tajawal',15))
        title.pack(fill=X)
        # ========= Variable ================
        self.q1=IntVar()
        self.q2=IntVar()
        self.q3=IntVar()
        self.q4=IntVar()
        self.q5=IntVar()
        self.q6=IntVar()
        self.q7=IntVar()
        self.q8=IntVar()
        self.q9=IntVar()
        self.q10=IntVar()
        self.q11=IntVar()
        self.q12=IntVar()
        self.q13=IntVar()
        self.q14=IntVar()
        self.q15=IntVar()
        self.q16=IntVar()
        self.q17=IntVar()
        self.q18=IntVar()
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq4=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.qq10=IntVar()
        self.qq11=IntVar()
        self.qq12=IntVar()
        self.qq13=IntVar()
        self.qq14=IntVar()
        self.qq15=IntVar()
        self.qq16=IntVar()
        self.qq17=IntVar()
        self.qq18=IntVar()
        self.qqq1=IntVar()
        self.qqq2=IntVar()
        self.qqq3=IntVar()
        self.qqq4=IntVar()
        self.qqq5=IntVar()
        self.qqq6=IntVar()
        self.qqq7=IntVar()
        self.qqq8=IntVar()
        self.qqq9=IntVar()
        self.qqq10=IntVar()
        self.qqq11=IntVar()
        self.qqq12=IntVar()
        self.qqq13=IntVar()
        self.qqq14=IntVar()
        self.qqq15=IntVar()

        self.bacoliat=StringVar()
        self.adoat=StringVar()
        self.kahraba=StringVar()

        self.nemo=StringVar()
        self.phono=StringVar()
        self.fatora=StringVar()
        x=random.randint(1000,9999)
        self.fatora.set(str(x))
        self.searcho=StringVar()
        # =========  Customer DATA ==========
        F1 = Frame(root,bd=2,width=338,height=170,bg='#0B4C5F')
        F1.place(x=961,y=35)
        tit = Label(F1,text=': بيانات المشتري ',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='tomato')
        tit.place(x=185,y=0)
        his_name = Label(F1,text='اسم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_name.place(x=230,y=40)
        his_phone = Label(F1,text='رقم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_phone.place(x=235,y=70)
        bill_num = Label(F1,text='رقم الفاتورة',font=('tajawal',10),bg='#0B4C5F',fg='white')
        bill_num.place(x=242,y=100)
        Ent_name=Entry(F1,justify='center',textvariable=self.nemo)
        Ent_name.place(x=90,y=42)
        Ent_phone=Entry(F1,justify='center',textvariable=self.phono)
        Ent_phone.place(x=90,y=72)
        Ent_bill=Entry(F1,justify='center',textvariable=self.fatora)
        Ent_bill.place(x=90,y=102)
        btn_customer = Button(F1, text='بحث',font=('tajawal',10),width=10,height=4,bg='white',command=self.find)
        btn_customer.place(x=3,y=40)
        titdd = Label(F1,text='[ الفواتير ]',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
        titdd.place(x=125,y=135)

        #======== Bill info =========
        F3 = Frame(root,bd=2,width=338,height=399,bg='white')
        F3.place(x=955,y=205)
        scrol_y= Scrollbar(F3,orient=VERTICAL)
        self.txtarea=Text(F3,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #======== Price =============
        F4 = Frame(root,bd=2,width=657,height=112,bg='#0B4C5F')
        F4.place(x=641,y=587)
        hesab=Button(F4,text='الحساب',width=13,height=1,font='tajawal',bg='#DBA901',command=self.total)
        hesab.place(x=537,y=10)
        fatora=Button(F4,text='تصدير فاتورة',width=13,height=1,font='tajawal',bg='#DBA901',command=self.billing)
        fatora.place(x=537,y=55)
        clear=Button(F4,text='افراغ الحقول',width=13,height=1,font='tajawal',bg='#DBA901',command=self.clear)
        clear.place(x=417,y=10)
        exite=Button(F4,text='اغلاق البرنامج',width=13,height=1,font='tajawal',bg='#DBA901')
        exite.place(x=417,y=55)
        lblo1=Label(F4,text='حساب الكلي البقوليات',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo1.place(x=220,y=10)
        lblo2=Label(F4,text='حساب اللوزام المنزلية',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo2.place(x=220,y=40)
        lblo3=Label(F4,text='حسـاب ادوات الـكهرباء',font=('tajawal',10,'bold'),bg='#0B4C5F',fg='gold')
        lblo3.place(x=220,y=70)
        ento1=Entry(F4,width=24,textvariable=self.bacoliat)
        ento1.place(x=40,y=12)
        ento2=Entry(F4,width=24,textvariable=self.adoat)
        ento2.place(x=40,y=42)
        ento3=Entry(F4,width=24,textvariable=self.kahraba)
        ento3.place(x=40,y=72)
        #======== Tools[1] ============
        FF1 = Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
        FF1.place(x=1,y=35)
        t = Label(FF1,text='الـبقوليات',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
        t.place(x=120,y=0)
        bq1=Label(FF1,text='الرز',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq1.place(x=250,y=50)
        bq2=Label(FF1,text='برغل',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq2.place(x=240,y=80)
        bq3=Label(FF1,text='فاصولياء',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq3.place(x=210,y=110)
        bq4=Label(FF1,text='عدس',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq4.place(x=232,y=140)
        bq5=Label(FF1,text='معكرونة',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq5.place(x=213,y=170)
        bq6=Label(FF1,text='فريكة',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq6.place(x=233,y=200)
        bq7=Label(FF1,text='حمص',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq7.place(x=228,y=230)
        bq8=Label(FF1,text='فول',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq8.place(x=240,y=270)
        bq9=Label(FF1,text='الملح',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq9.place(x=230,y=300)
        bq10=Label(FF1,text='سكر',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq10.place(x=233,y=330)
        bq11=Label(FF1,text='فلفل اسود',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq11.place(x=200,y=370)
        bq12=Label(FF1,text='فلفل احمر',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq12.place(x=200,y=400)
        bq13=Label(FF1,text='اللوبيا ',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq13.place(x=230,y=430)
        bq14=Label(FF1,text=' الادمامي',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq14.place(x=210,y=470)
        bq15=Label(FF1,text='القمح ',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq15.place(x=230,y=500)
        bq16=Label(FF1,text='الشعير ',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq16.place(x=220,y=530)
        bq17=Label(FF1,text='الشوفان ',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq17.place(x=210,y=570)
        bq18=Label(FF1,text=' الذرة',font=('tajawal',11),bg='#0B4C5F',fg='white')
        bq18.place(x=230,y=600)
        bqent1=Entry(FF1,width=12,textvariable=self.q1)
        bqent1.place(x=70,y=50)
        bqent2=Entry(FF1,width=12,textvariable=self.q2)
        bqent2.place(x=70,y=80)
        bqent3=Entry(FF1,width=12,textvariable=self.q3)
        bqent3.place(x=70,y=110)
        bqent4=Entry(FF1,width=12,textvariable=self.q4)
        bqent4.place(x=70,y=140)
        bqent5=Entry(FF1,width=12,textvariable=self.q5)
        bqent5.place(x=70,y=170)
        bqent6=Entry(FF1,width=12,textvariable=self.q6)
        bqent6.place(x=70,y=200)
        bqent7=Entry(FF1,width=12,textvariable=self.q7)
        bqent7.place(x=70,y=230)
        bqent8=Entry(FF1,width=12,textvariable=self.q8)
        bqent8.place(x=70,y=270)
        bqent9=Entry(FF1,width=12,textvariable=self.q9)
        bqent9.place(x=70,y=300)
        bqent10=Entry(FF1,width=12,textvariable=self.q10)
        bqent10.place(x=70,y=330)
        bqent11=Entry(FF1,width=12,textvariable=self.q11)
        bqent11.place(x=70,y=370)
        bqent12=Entry(FF1,width=12,textvariable=self.q12)
        bqent12.place(x=70,y=400)
        bqent13=Entry(FF1,width=12,textvariable=self.q13)
        bqent13.place(x=70,y=430)
        bqent14=Entry(FF1,width=12,textvariable=self.q14)
        bqent14.place(x=70,y=480)
        bqent15=Entry(FF1,width=12,textvariable=self.q15)
        bqent15.place(x=70,y=510)
        bqent16=Entry(FF1,width=12,textvariable=self.q16)
        bqent16.place(x=70,y=540)
        bqent17=Entry(FF1,width=12,textvariable=self.q17)
        bqent17.place(x=70,y=570)
        bqent18=Entry(FF1,width=12,textvariable=self.q18)
        bqent18.place(x=70,y=600)


        #==========  Tools[2] ===============
        FF2 = Frame(root,bd=2,width=318,height=664,bg='#0B4C5F')
        FF2.place(x=321,y=35)
        tt = Label(FF2,text='اللوازم المنزلية',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
        tt.place(x=120,y=0)
        bqr1=Label(FF2,text='مصفاة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr1.place(x=228,y=50)
        bqr2=Label(FF2,text='صحن',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr2.place(x=233,y=80)
        bqr3=Label(FF2,text='كأس',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr3.place(x=234,y=110)
        bqr4=Label(FF2,text='ابريق',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr4.place(x=237,y=140)
        bqr5=Label(FF2,text='سكين',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr5.place(x=226,y=170)
        bqr6=Label(FF2,text='شوك',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr6.place(x=233,y=200)
        bqr7=Label(FF2,text='طنجرة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr7.place(x=228,y=230)
        bqr8=Label(FF2,text='سلة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr8.place(x=240,y=270)
        bqr9=Label(FF2,text='ملاعق',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr9.place(x=230,y=300)
        bqr10=Label(FF2,text='صينية',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr10.place(x=233,y=330)
        bqr11=Label(FF2,text='وعاء الخلط',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr11.place(x=200,y=370)
        bqr12=Label(FF2,text='فتاحة علب',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr12.place(x=200,y=400)
        bqr13=Label(FF2,text='مقشرة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr13.place(x=220,y=430)
        bqr14=Label(FF2,text='لوح التقطيع',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr14.place(x=190,y=470)
        bqr15=Label(FF2,text='حفارة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr15.place(x=230,y=500)
        bqr16=Label(FF2,text='سلة قمامة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr16.place(x=196,y=530)
        bqr17=Label(FF2,text='منفضة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr17.place(x=219,y=570)
        bqr18=Label(FF2,text='اكياس',font=('tajawal',12),bg='#0B4C5F',fg='white')
        bqr18.place(x=225,y=600)
        bqrnt1=Entry(FF2,width=12,textvariable=self.qq1)
        bqrnt1.place(x=70,y=50)
        bqrnt2=Entry(FF2,width=12,textvariable=self.qq2)
        bqrnt2.place(x=70,y=80)
        bqrnt3=Entry(FF2,width=12,textvariable=self.qq3)
        bqrnt3.place(x=70,y=110)
        bqrnt4=Entry(FF2,width=12,textvariable=self.qq4)
        bqrnt4.place(x=70,y=140)
        bqrnt5=Entry(FF2,width=12,textvariable=self.qq5)
        bqrnt5.place(x=70,y=170)
        bqrnt6=Entry(FF2,width=12,textvariable=self.qq6)
        bqrnt6.place(x=70,y=200)
        bqrnt7=Entry(FF2,width=12,textvariable=self.qq7)
        bqrnt7.place(x=70,y=230)
        bqrnt8=Entry(FF2,width=12,textvariable=self.qq8)
        bqrnt8.place(x=70,y=270)
        bqrnt9=Entry(FF2,width=12,textvariable=self.qq9)
        bqrnt9.place(x=70,y=300)
        bqrnt10=Entry(FF2,width=12,textvariable=self.qq10)
        bqrnt10.place(x=70,y=330)
        bqrnt11=Entry(FF2,width=12,textvariable=self.qq11)
        bqrnt11.place(x=70,y=370)
        bqrnt12=Entry(FF2,width=12,textvariable=self.qq12)
        bqrnt12.place(x=70,y=400)
        bqrnt13=Entry(FF2,width=12,textvariable=self.qq13)
        bqrnt13.place(x=70,y=430)
        bqrnt14=Entry(FF2,width=12,textvariable=self.qq14)
        bqrnt14.place(x=70,y=480)
        bqrnt15=Entry(FF2,width=12,textvariable=self.qq15)
        bqrnt15.place(x=70,y=510)
        bqrnt16=Entry(FF2,width=12,textvariable=self.qq16)
        bqrnt16.place(x=70,y=540)
        bqrnt17=Entry(FF2,width=12,textvariable=self.qq17)
        bqrnt17.place(x=70,y=570)
        bqrnt18=Entry(FF2,width=12,textvariable=self.qq18)
        bqrnt18.place(x=70,y=600)




        #====== Tools[3] =================
        FF3 = Frame(root,bd=2,width=318,height=550,bg='#0B4C5F')
        FF3.place(x=641,y=35)
        ttt = Label(FF3,text='ادوات كهربائية',font=('tajawal',13,'bold'),bg='#0B4C5F',fg='gold')
        ttt.place(x=120,y=0)
        br1=Label(FF3,text='مكنسة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br1.place(x=228,y=50)
        br2=Label(FF3,text='تلفزيون',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br2.place(x=233,y=80)
        br3=Label(FF3,text='غسالة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br3.place(x=234,y=110)
        br4=Label(FF3,text='مكرويف',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br4.place(x=230,y=140)
        br5=Label(FF3,text='خلاط',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br5.place(x=243,y=170)
        br6=Label(FF3,text='فرن غاز',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br6.place(x=233,y=200)
        br7=Label(FF3,text='مقلاة كهرباء',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br7.place(x=195,y=230)
        br8=Label(FF3,text='مروحة سقف',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br8.place(x=200,y=270)
        br9=Label(FF3,text='مروحة ارضية',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br9.place(x=200,y=300)
        br10=Label(FF3,text='تلفزيون 32',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br10.place(x=210,y=330)
        br11=Label(FF3,text='تلفزيون 43',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br11.place(x=210,y=370)
        br12=Label(FF3,text='فلتر ماء',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br12.place(x=230,y=400)
        br13=Label(FF3,text='غسالة اوتو',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br13.place(x=210,y=430)
        br14=Label(FF3,text='مكواة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br14.place(x=240,y=470)
        br15=Label(FF3,text='مبردة',font=('tajawal',12),bg='#0B4C5F',fg='white')
        br15.place(x=243,y=500)
        bqnt1=Entry(FF3,width=12,textvariable=self.qqq1)
        bqnt1.place(x=70,y=50)
        bqnt2=Entry(FF3,width=12,textvariable=self.qqq2)
        bqnt2.place(x=70,y=80)
        bqnt3=Entry(FF3,width=12,textvariable=self.qqq3)
        bqnt3.place(x=70,y=110)
        bqnt4=Entry(FF3,width=12,textvariable=self.qqq4)
        bqnt4.place(x=70,y=140)
        bqnt5=Entry(FF3,width=12,textvariable=self.qqq5)
        bqnt5.place(x=70,y=170)
        bqnt6=Entry(FF3,width=12,textvariable=self.qqq6)
        bqnt6.place(x=70,y=200)
        bqnt7=Entry(FF3,width=12,textvariable=self.qqq7)
        bqnt7.place(x=70,y=230)
        bqnt8=Entry(FF3,width=12,textvariable=self.qqq8)
        bqnt8.place(x=70,y=270)
        bqnt9=Entry(FF3,width=12,textvariable=self.qqq9)
        bqnt9.place(x=70,y=300)
        bqnt10=Entry(FF3,width=12,textvariable=self.qqq10)
        bqnt10.place(x=70,y=330)
        bqnt11=Entry(FF3,width=12,textvariable=self.qqq11)
        bqnt11.place(x=70,y=370)
        bqnt12=Entry(FF3,width=12,textvariable=self.qqq12)
        bqnt12.place(x=70,y=400)
        bqnt13=Entry(FF3,width=12,textvariable=self.qqq13)
        bqnt13.place(x=70,y=430)
        bqnt14=Entry(FF3,width=12,textvariable=self.qqq14)
        bqnt14.place(x=70,y=480)
        bqnt15=Entry(FF3,width=12,textvariable=self.qqq15)
        bqnt15.place(x=70,y=510)
        self.welcome()
    def total(self):
        self.rez= self.q1.get()*1.5
        self.borgel = self.q2.get()*0.5
        self.fasoli = self.q3.get()*1
        self.ades = self.q4.get()*1.5
        self.makrona = self.q5.get()*2
        self.frika = self.q6.get()*2
        self.homes = self.q7.get()*1
        self.fol = self.q8.get()*1
        self.mlah = self.q9.get()*1.5
        self.skar = self.q10.get()*1
        self.flflahmar = self.q11.get()*1.5
        self.flflasoad = self.q12.get()*1
        self.lobia = self.q13.get()*1.5
        self.admami = self.q14.get()*1
        self.qmah = self.q15.get()*2
        self.shair = self.q16.get()*1
        self.shofan = self.q17.get()*2
        self.zara = self.q18.get()*1.5
        self.totalito=float(
                        self.rez+
                        self.borgel+
                        self.fasoli+
                        self.ades+
                        self.makrona+
                        self.frika+
                        self.homes+
                        self.fol+
                        self.mlah+
                        self.skar+
                        self.flflahmar+
                        self.flflasoad+
                        self.lobia+
                        self.admami+
                        self.qmah+
                        self.shair+
                        self.shofan+
                        self.zara
                        )
        self.bacoliat.set(str(self.totalito)+" $")
        self.rez2= self.qqq1.get()*30
        self.borgel2 = self.qqq2.get()*140
        self.fasoli2 = self.qqq3.get()*300
        self.ades2 = self.qqq4.get()*40
        self.makrona2 = self.qqq5.get()*15
        self.frika2 = self.qqq6.get()*110
        self.homes2 = self.qqq7.get()*20
        self.fol2 = self.qqq8.get()*10
        self.mlah2 = self.qqq9.get()*15
        self.skar2 = self.qqq10.get()*140
        self.flflahmar2 = self.qqq11.get()*230
        self.flflasoad2 = self.qqq12.get()*130
        self.lobia2 = self.qqq13.get()*430
        self.admami2 = self.qqq14.get()*15
        self.qmah2 = self.qqq15.get()*90
        self.khrba=float(
                        self.rez2+
                        self.borgel2+
                        self.fasoli2+
                        self.ades2+
                        self.makrona2+
                        self.frika2+
                        self.homes2+
                        self.fol2+
                        self.mlah2+
                        self.skar2+
                        self.flflahmar2+
                        self.flflasoad2+
                        self.lobia2+
                        self.admami2+
                        self.qmah2
                        )
        self.kahraba.set(str(self.khrba)+" $")
        self.rez1= self.qq1.get()*1.5
        self.borgel1 = self.qq2.get()*0.5
        self.fasoli1 = self.qq3.get()*1
        self.ades1 = self.qq4.get()*1.5
        self.makrona1 = self.qq5.get()*2
        self.frika1 = self.qq6.get()*2
        self.homes1 = self.qq7.get()*1
        self.fol1 = self.qq8.get()*1
        self.mlah1 = self.qq9.get()*1.5
        self.skar1 = self.qq10.get()*1
        self.flflahmar1 = self.qq11.get()*1.5
        self.flflasoad1 = self.qq12.get()*1
        self.lobia1 = self.qq13.get()*1.5
        self.admami1 = self.qq14.get()*1
        self.qmah1 = self.qq15.get()*2
        self.shair1 = self.qq16.get()*1
        self.shofan1 = self.qq17.get()*2
        self.zara1 = self.qq18.get()*1.5
        self.adoatdd=float(
                        self.rez1+
                        self.borgel1+
                        self.fasoli1+
                        self.ades1+
                        self.makrona1+
                        self.frika1+
                        self.homes1+
                        self.fol1+
                        self.mlah1+
                        self.skar1+
                        self.flflahmar1+
                        self.flflasoad1+
                        self.lobia1+
                        self.admami1+
                        self.qmah1+
                        self.shair1+
                        self.shofan1+
                        self.zara1
                        )
        self.adoat.set(str(self.adoatdd)+" $")
        self.all=float(self.totalito+
                       self.khrba+
                       self.adoatdd
                       )
    def welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tسوبر ماركت الخبير يرحب بكم")
        self.txtarea.insert(END,"\n  ====================================")
        self.txtarea.insert(END,f"\n\t B.NUM  : {self.fatora.get()}")
        self.txtarea.insert(END,f"\n\t Name   : {self.nemo.get()}")
        self.txtarea.insert(END,f"\n\t Phone  : {self.phono.get()}")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,f"\nالسعر\t      العدد\t       المشتريات ")
        self.txtarea.insert(END,"\n======================================")



    def billing(self):
        if self.nemo.get()=="" or self.phono.get()=="":
            messagebox.showerror("حدث خطأ","لا يجوز ترك حقل الاسم ورقم الهاتف فارغا")
        elif self.bacoliat.get()=="0.0 $" and self.adoat.get()=="0.0 $" and self.kahraba.get()=="0.0 $":
            messagebox.showerror("حدث خطأ"," ليس هناك منتجات محددة ولم يتم اختيار احداها يجب اختيار عدد المنتجات")
        else:
            self.welcome()
            if self.q1.get()!=0:
                self.txtarea.insert(END,f"\n {self.rez}\t\t{self.q1.get()}\t\tالرز ")
            if self.q2.get()!=0:
                self.txtarea.insert(END,f"\n {self.borgel}\t\t{self.q2.get()}\t\tبرغل ")
            if self.q3.get()!=0:
                self.txtarea.insert(END,f"\n {self.fasoli}\t\t{self.q3.get()}\t\tفاصولياء ")
            if self.q4.get()!=0:
                self.txtarea.insert(END,f"\n {self.ades}\t\t{self.q4.get()}\t\tعدس ")
            if self.q5.get()!=0:
                self.txtarea.insert(END,f"\n {self.makrona}\t\t{self.q5.get()}\t\tمعكرونة ")
            if self.q6.get()!=0:
                self.txtarea.insert(END,f"\n {self.frika}\t\t{self.q6.get()}\t\tفريكة ")
            if self.q7.get()!=0:
                self.txtarea.insert(END,f"\n {self.homes}\t\t{self.q7.get()}\t\tحمص ")
            if self.q8.get()!=0:
                self.txtarea.insert(END,f"\n {self.fol}\t\t{self.q8.get()}\t\tفول ")
            if self.q9.get()!=0:
                self.txtarea.insert(END,f"\n {self.mlah}\t\t{self.q9.get()}\t\tملح ")
            if self.q10.get()!=0:
                self.txtarea.insert(END,f"\n {self.skar}\t\t{self.q10.get()}\t\tسكر ")
            if self.q11.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflasoad}\t\t{self.q11.get()}\t  فلفل اسود ")
            if self.q12.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflahmar}\t\t{self.q12.get()}\t  فلفل احمر ")
            if self.q13.get()!=0:
                self.txtarea.insert(END,f"\n {self.lobia}\t\t{self.q13.get()}\t\tاللوبيا ")
            if self.q14.get()!=0:
                self.txtarea.insert(END,f"\n {self.admami}\t\t{self.q14.get()}\t\tادمامي ")
            if self.q15.get()!=0:
                self.txtarea.insert(END,f"\n {self.qmah}\t\t{self.q15.get()}\t\tالقمح ")
            if self.q16.get()!=0:
                self.txtarea.insert(END,f"\n {self.shair}\t\t{self.q16.get()}\t\tالشعير ")
            if self.q17.get()!=0:
                self.txtarea.insert(END,f"\n {self.shofan}\t\t{self.q17.get()}\t\tالشوفان ")
            if self.q18.get()!=0:
                self.txtarea.insert(END,f"\n {self.zara}\t\t{self.q18.get()}\t\tالذرة ")



            if self.qq1.get()!=0:
                self.txtarea.insert(END,f"\n {self.rez1}\t\t{self.qq1.get()}\t\tمصفاة")
            if self.qq2.get()!=0:
                self.txtarea.insert(END,f"\n {self.borgel1}\t\t{self.qq2.get()}\t\tصحن")
            if self.qq3.get()!=0:
                self.txtarea.insert(END,f"\n {self.fasoli1}\t\t{self.qq3.get()}\t\tكأس")
            if self.qq4.get()!=0:
                self.txtarea.insert(END,f"\n {self.ades1}\t\t{self.qq4.get()}\t\tابريق")
            if self.qq5.get()!=0:
                self.txtarea.insert(END,f"\n {self.makrona1}\t\t{self.qq5.get()}\t\tسكين")
            if self.qq6.get()!=0:
                self.txtarea.insert(END,f"\n {self.frika1}\t\t{self.qq6.get()}\t\tشوك")
            if self.qq7.get()!=0:
                self.txtarea.insert(END,f"\n {self.homes1}\t\t{self.qq7.get()}\t\tطنجرة")
            if self.qq8.get()!=0:
                self.txtarea.insert(END,f"\n {self.fol1}\t\t{self.qq8.get()}\t\tسلة")
            if self.qq9.get()!=0:
                self.txtarea.insert(END,f"\n {self.mlah1}\t\t{self.qq9.get()}\t\tملاعق")
            if self.qq10.get()!=0:
                self.txtarea.insert(END,f"\n {self.skar1}\t\t{self.qq10.get()}\t\tصينية")
            if self.qq11.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflasoad1}\t\t{self.qq11.get()}\t   وعاد الخلط")
            if self.qq12.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflahmar1}\t\t{self.qq12.get()}\t   فتاحة علب")
            if self.qq13.get()!=0:
                self.txtarea.insert(END,f"\n {self.lobia1}\t\t{self.qq13.get()}\t\tمقشرة")
            if self.qq14.get()!=0:
                self.txtarea.insert(END,f"\n {self.admami1}\t\t{self.qq14.get()}\t   لوح التقطيع")
            if self.q15.get()!=0:
                self.txtarea.insert(END,f"\n {self.qmah1}\t\t{self.qq15.get()}\t\tحفارة")
            if self.qq16.get()!=0:
                self.txtarea.insert(END,f"\n {self.shair1}\t\t{self.qq16.get()}\t   سلة قمامة")
            if self.qq17.get()!=0:
                self.txtarea.insert(END,f"\n {self.shofan1}\t\t{self.qq17.get()}\t\tمنفضة")
            if self.qq18.get()!=0:
                self.txtarea.insert(END,f"\n {self.zara1}\t\t{self.qq18.get()}\t\tاكياس")

            if self.qqq1.get()!=0:
                self.txtarea.insert(END,f"\n {self.rez1}\t\t{self.qqq1.get()}\t\tمكنسة")
            if self.qqq2.get()!=0:
                self.txtarea.insert(END,f"\n {self.borgel2}\t\t{self.qqq2.get()}\t  تلفزيون")
            if self.qqq3.get()!=0:
                self.txtarea.insert(END,f"\n {self.fasoli2}\t\t{self.qqq3.get()}\t\tغسالة")
            if self.qqq4.get()!=0:
                self.txtarea.insert(END,f"\n {self.ades2}\t\t{self.qqq4.get()}\t\tمكرويف")
            if self.qqq5.get()!=0:
                self.txtarea.insert(END,f"\n {self.makrona2}\t\t{self.qqq5.get()}\t\tخلاط")
            if self.qqq6.get()!=0:
                self.txtarea.insert(END,f"\n {self.frika2}\t\t{self.qqq6.get()}\t   فرن غاز")
            if self.qqq7.get()!=0:
                self.txtarea.insert(END,f"\n {self.homes2}\t\t{self.qqq7.get()}\t\tمقلاة")
            if self.qqq8.get()!=0:
                self.txtarea.insert(END,f"\n {self.fol2}\t\t{self.qqq8.get()}\t   مروحة سقف")
            if self.qqq9.get()!=0:
                self.txtarea.insert(END,f"\n {self.mlah2}\t\t{self.qqq9.get()}\t   مروحة ارض")
            if self.qqq10.get()!=0:
                self.txtarea.insert(END,f"\n {self.skar2}\t\t{self.qqq10.get()}\t   تلفزيون32")
            if self.qqq11.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflasoad2}\t\t{self.qqq11.get()}\t   تلفزيون43")
            if self.qqq12.get()!=0:
                self.txtarea.insert(END,f"\n {self.flflahmar2}\t\t{self.qqq12.get()}\t   فلتر ماء")
            if self.qqq13.get()!=0:
                self.txtarea.insert(END,f"\n {self.lobia2}\t\t{self.qqq13.get()}\t   غسالة اوتو")
            if self.qqq14.get()!=0:
                self.txtarea.insert(END,f"\n {self.admami2}\t\t{self.qqq14.get()}\t\tمكواة")
            if self.qqq15.get()!=0:
                self.txtarea.insert(END,f"\n {self.qmah2}\t\t{self.qqq15.get()}\t\tمبردة")

            self.txtarea.insert(END,"\n......................................")
            self.txtarea.insert(END,f"\n\t{self.all} $\t     المجموع الكلي")
            self.txtarea.insert(END,"\n......................................")
            self.savee()
    






    def savee(self):
        op = messagebox.askyesno("هل تريد حفظ الفاتورة ؟","حفظ")
        if op > 0 :
            self.bb = self.txtarea.get('1.0',END)
            f1 = open('D:\\buy\\'+str(self.fatora.get())+".txt","w",encoding="utf-8")
            f1.write(self.bb)
            f1.close()
        else:
            return














    def find(self):
        present="no"
        for i in os.listdir("D:\\buy\\"):
            if i.split('.')[0] == self.fatora.get():
                f1=open(f"D:\\buy\\{i}","r",encoding="utf-8")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                self.txtarea.insert(END,'')
                f1.close()
                present="yes"
        if present == "no":
                messagebox.showerror('خطأ',' لا توجد اي فاتورة تحمل الرقم الذي كتبته  ')
    def clear(self):
        self.q1.set(0)
        self.q2.set(0)
        self.q3.set(0)
        self.q4.set(0)
        self.q5.set(0)
        self.q6.set(0)
        self.q7.set(0)
        self.q8.set(0)
        self.q9.set(0)
        self.q10.set(0)
        self.q11.set(0)
        self.q12.set(0)
        self.q13.set(0)
        self.q14.set(0)
        self.q15.set(0)
        self.q16.set(0)
        self.q17.set(0)
        self.q18.set(0)
        self.qq1.set(0)
        self.qq2.set(0)
        self.qq3.set(0)
        self.qq4.set(0)
        self.qq5.set(0)
        self.qq6.set(0)
        self.qq7.set(0)
        self.qq8.set(0)
        self.qq9.set(0)
        self.qq10.set(0)
        self.qq11.set(0)
        self.qq12.set(0)
        self.qq13.set(0)
        self.qq14.set(0)
        self.qq15.set(0)
        self.qq16.set(0)
        self.qq17.set(0)
        self.qq18.set(0)
        self.qqq1.set(0)
        self.qqq2.set(0)
        self.qqq3.set(0)
        self.qqq4.set(0)
        self.qqq5.set(0)
        self.qqq6.set(0)
        self.qqq7.set(0)
        self.qqq8.set(0)
        self.qqq9.set(0)
        self.qqq10.set(0)
        self.qqq11.set(0)
        self.qqq12.set(0)
        self.qqq13.set(0)
        self.qqq14.set(0)
        self.qqq15.set(0)
        self.bacoliat.set(0)
        self.adoat.set(0)
        self.kahraba.set(0)
        self.nemo.set('')
        self.phono.set('')
        self.fatora.set('')
root =Tk()
ob=Super(root)
root.mainloop()