print('--------------------------------------------------------')
print('--------WELCOME TO HOMEOPATHIC EXPERT SYSTEM---------- |')
print('enter which category do you want diagnosis             |')
print('1.children                                             |')
print('2.digestive                                            |')
print('3.fever and general                                    |')
print('4.joints and muscles                                   |')
print('5.respiratory diseases                                 |')
print('6.skin diseases                                        |')
print('7.Lifestyle diseses                                    |')
print('--------------------------------------------------------')
b=[]
while(1):
    a=int(input())
    
    if(a==1):
        print('eneter which in which problems you want diagnosis')
        print('1.hyper active')
        print('2.bedwetting')
        print('3.cold')
        print('4.growth deficiency')
        print('5.fever')
        print('6.clacium deficiency')
        print('7.cough')
        b1=input().split(' ')
        if '1' in b1:
             b.append('KINDIVAL')
        if '2' in b1:
             b.append('ENUKIND')
        if '3' in b1:
             b.append('NISIKIND')
        if '4' in b1:
             b.append('ANEKIND')
        if '5' in b1:
             b.append('ECHINACEA ANGUSTIFOLIA 1X')
        if '6' in b1:
             b.append('CALCIOKIND')
        if '7' in b1:
             b.append('TUSSIKIND')
        print('the count is ',len(b))
        print('the medicine list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==3):
        print('enter which in which problems you want diagnosis')
        print('1.fever')
        print('2.immune boosters')
        print('3.tonsilities')
        print('4.vomiting sensation')
        print('5.chill')
        print('6.cold')
        print('7.cough')
        b1=input().split()
        if '1' in b1:
            b.append('ACONITUM PENTARKAN')
        if '2' in b1:
              b.append('MUNOSTIM')
        if '3' in b1:
              b.append('ALPHA-TONS')
        if '4' in b1:
            b.append('ALPHA-LIV')
        if '5' in b1:
              b.append('ALPHA-WD')
        if '6' in b1:
              b.append('NUSIKIND')
        if '7' in b1:
             b.append('TUSSIKIND')
        print('the count is ',len(b))
        print('the medicine list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==2):
        print('enter which in which problems you want diagnosis')
        print('1.diarrhoea')
        print('2.vomitings')
        print('3.acidity')
        print('4.colic')
        print('5.nausea')
        print('6.motion sickness')
        print('7.loss of apetetite')
        print('8.travel sickness')
        print('9.constipation')
        print('10.dysentry')
        b1=input().split()
        if '1' in b1:
            b.append('BIOCOMBINATION NO. 08')
        if '2' in b1:
            b.append('ALPHA-MS')
        if '3' in b1:
            b.append('ALPHA-ACID')
        if '4' in b1:
            b.append('COLIKIND')
        if '5' in b1:
            b.append('KINDIGEST')
        if '6' in b1:
            b.append('ALPHA-MS')
        if '7' in b1:
            b.append('ALPHA-LIV')
        if '8' in b1:
            b.append('ALPHA-MS')
        if '9' in b1:
            b.append('NATRUM MURIATICUM')
        if '10' in b1:
            b.append('HOLARRHENA ANTIDYSENTERICA 1X')
        print('the count is ',len(b))
        print('the list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==4):
        print('enter which in which problems you want diagnosis')
        print('1.cramps')
        print('2.muscular pain')
        print('3.rheamtic pain')
        print('4.bone problems')
        print('5.body ache')
        print('6.joints')
        print('7.inflammation')
        print('8.muscles')
        print('9.spasms')
        print('10.Osteoarthritis')
        b1=input().split()
        if '1' in b1:
            b.append('MAGNESIUM PHOSPHORICUM')
        if '2' in b1:
            b.append('Alpha-MP')
        if '3' in b1:
            b.append('Alpha-MP')
        if '4' in b1:
            b.append('Calcarea phosphorica')
        if '5' in b1:
            b.append('TOPI ARNICA CREAM')
        if '6' in b1:
            b.append('Topi MP Gel')
        if '7' in b1:
            b.append('Topi Heal Cream')
        if '8' in b1:
            b.append('Kali phosphoricum')
        if '9' in b1:
            b.append('Magnesium Phosphoricum Pentarkan')
        if '10' in b1:
            b.append('Biocombination No. 19')
        print('the count is ',len(b))
        print('the list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==5):
        print('enter which in which problems you want diagnosis')
        print('1.Chronic Cough')
        print('2.Spasmodic cough')
        print('3.Cough syrup')
        print('4.Irritating cough')
        print('5.Nasal congestion')
        print('6.Sneezing')
        print('7.Stuffiness of nostrils')
        print('8.Breathlessness')
        print('9.Coryza')
        print('10.respiratory congestion')
        b1=input().split()
        if '1' in b1:
            b.append('Alpha-CC')
        if '2' in b1:
            b.append('Alpha-Coff')
        if '3' in b1:
            b.append('Aconitum Pentarkan')
        if '4' in b1:
            b.append('Glycyrrhiza glabra 1X')
        if '5' in b1:
            b.append('Alpha-NC')
        if '6' in b1:
            b.append('Alpha-RC')
        if '7' in b1:
            b.append('Alpha-NC2')
        if '8' in b1:
            b.append('Alpha-RC1')
        if '9' in b1:
            b.append('BIOCOMBINATION NO. 05')
        if '10' in b1:
            b.append('Biocombination No. 13')
        print('the count is ',len(b))
        print('the list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==6):
        print('enter in which of the following you want diagnosis')
        print('1.Acne')
        print('2.pimples')
        print('3.psoriasis')
        print('4.bed sores')
        print('5.boils')
        print('6.cuts')
        print('7.itching')
        print('8.scabies')
        print('9.dermatities')
        print('10.fungal infection')
        b1=input().split()
        if '1' in b1:
            b.append('TOPI BERBERIS CREAM')
        if '2' in b1:
            b.append('Calcarea sulphurica')
        if '3' in b1:
            b.append('Alpha-WD')
        if '4' in b1:
            b.append('Topi Heal Cream')
        if '5' in b1:
            b.append('Silicea')
        if '6' in b1:
            b.append('Hepar Sulphuris Pentarkan')
        if '7' in b1:
            b.append('Graphites Pentarkan')
        if '8' in b1:
            b.append('Topi Sulphur Cream')
        if '9' in b1:
            b.append('B&T Akne - Sor Soap')
        if '10' in b1:
            b.append('B&T CALENDULA & ALOE VERA MULTIPURPOSE CREAM')
        print('the count is ',len(b))
        print('the list is ',b)
        print('even after the use of medicines you are not comfortable consult the doctor')
        break
    elif(a==7):
         print('enter in which of the following you want diagnosis')
         print('1.weight loss')
         print('2.tension and stress')
         print('3.insomnia')
         print('4.erectile disfunction')
         print('5.hyper tension')
         print('6.mental stress')
         print('7.obesity')
         print('8.alcoholism')
         print('9.thyroid disorder')
         print('10.stress bustor')
         b1=input().split()
         if '1' in b1:
            b.append('Phytolacca Berry Tablets')
         if '2' in b1:
            b.append('Alpha-TS')
         if '3' in b1:
            b.append('Kali phosphoricum')
         if '4' in b1:
            b.append('Damiaplant')
         if '5' in b1:
            b.append('Essentia aurea')
         if '6' in b1:
            b.append('Ginseng 1X')
         if '7' in b1:
            b.append('Phytolacca Berry Tablets*')
         if '8' in b1:
            b.append('Quercus robur 1x')
         if '9' in b1:
            b.append('Thyroidinum 3X (LATT)')
         if '10' in b1:
            b.append('Biocombination No. 03')
         print('the count is ',len(b))
         print('the list is ',b)
         print('even after the use of medicines you are not comfortable consult the doctor')
         break
         
    else:
        print('please enter a valid option')
