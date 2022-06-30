%DUPLA: Layla Couto
gerou(djalma, marivaldo).
gerou(francisca, marivaldo).
gerou(djalma, nilda).
gerou(francisca, nilda).
gerou(djalma, maria).
gerou(francisca, maria).
gerou(marivaldo, aurelio).
gerou(josiane, aurelio).
gerou(marivaldo, layla).
gerou(josiane, layla).

homem(djalma).
homem(marivaldo).
homem(aurelio).

mulher(francisca).
mulher(nilda).
mulher(maria).
mulher(josiane).
mulher(layla).

lugar(colatina).
lugar(brasil).

nasceuEm(djalma,colatina).
nasceuEm(francisca,colatina).
nasceuEm(maria,colatina).
nasceuEm(nida,colatina).
nasceuEm(marivaldo,colatina).
nasceuEm(josiane,colatina).
nasceuEm(aurelio,colatina).
nasceuEm(layla,colatina).

pertenceA(colatina,brasil).

paiDe(X,Y):- gerou(X,Y),homem(X).
