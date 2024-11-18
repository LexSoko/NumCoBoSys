%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Matrixelemente des Heisenbergmagnet
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [result, basis] = matelem(Sz, Jz, Jp, Nx, Ny);

[lattice nn] = tabcoord(Nx, Ny, 1);

list = 0;
n = Nx*Ny/2 - Sz;
for i = 1:(Nx*Ny/2 + Sz)
  list = list + 2^(i-1);
end;
for i = 1:n
  pos(i) = Nx*Ny/2+Sz+i;
end;  
%keyboard;
basis = create2(list,pos,n);

N = size(basis,2);
%keyboard;

H = sparse(N,N);

for i = 1:N
  st = basis(i);
  H(i,i) = Jz/4*(2 * bitget(st, nn(:,1)) - 1)' * (2 * bitget(st, nn(:,2)) - 1);
end;

for i = 1:N
  for k = 1:size(nn,1)
     l = nn(k,1);
     m = nn(k,2);
     bitl = bitget(basis(i),l);
     bitm = bitget(basis(i),m);
     if (bitl~= bitm)
       state = bitset(basis(i), l, bitm);
       state = bitset(state, m, bitl);
       y = such(basis, state, 1, N);
       H(y, i) = H(y, i) + Jp/2;
       %keyboard;    
     end;  
  end;   
end;   

result = H;
%H = sparse(H);

%keyboard;



