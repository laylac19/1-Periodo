%DUPLA: Layla Couto e Bruno Martinelli
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


gerou(cecilia, fabio).
gerou(cecilia, kesy).
gerou(cecilia, elaine).
gerou(cecilia, daiane).
gerou(jair, fabio).
gerou(jair, kesy).
gerou(jair, elaine).
gerou(jair, daiane).

gerou(rosely, bruno).
gerou(rosely, fabiojr).
gerou(fabio, bruno).
gerou(fabio, fabiojr).


homem(djalma).
homem(marivaldo).
homem(aurelio).

homem(andre).
homem(jair).
homem(fabio).
homem(sidney).
homem(bruno).
homem(fabiojr).

mulher(francisca).
mulher(josiane).
mulher(layla).

mulher(maria).
mulher(cecilia).
mulher(rosely).
mulher(eloisa).
mulher(rosangela).
mulher(marli).
mulher(kesy).
mulher(daiane).
mulher(elaine).

%%Obter todos os irm?os de um dos alunos:
%?- gerou(X, layla), gerou(X, Y), Y\= layla.

%%Obter os av?s paternos de um dos alunos
%?- gerou(X, Y), gerou(Y, layla).

%Obter todas as duplas pai/filho da base;
%?- gerou(X, Y).

%Obter as cunhadas da m?e do aluno:
%?- gerou(X, marivaldo), gerou(X, Y), mulher(Y).

%Obter quem ? homem na fam?lia do aluno:
%?- homem(X).

%Obter quem ? homem na fam?lia do aluno:
%?- mulher(X).

%% Obter todos os tios de um dos alunos:
% gerou(andre, X), homem(X).

% Obter todas as duplas pai/filho da base:
% gerou(X, Y),homem(X),homem(Y).

% Obter todas as duplas av?/neto providos da m?e do aluno:
% gerou(X, rosely), gerou(rosely, Y), mulher(X), homem(Y).
