%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Erzeugt alle Permutationen eines Bitmusters
%  (C) 2000 Markus Aichhorn
%
%  Aufruf: list = create(start, start, pos, n, n)
%  start : Ausgangsbitmuster: alle Nullen ganz links
%  pos : array mit den Positionen der Nullen (von rechts weggezählt) 
%  n : Anzahl der Nullen
%  z.B.: bei 4 Nullen und 3 Einsen: start = (0000111) = 7
%						pos = [4 5 6 7]
%						n = 4
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


function result = create2(list, pos, n);

i=n;
temp = list;

%keyboard;
while (pos(n) > n)
%disp('.');
if (pos(i) > i)
   h = 0;
   while (bitget(temp, pos(i) - h - 1) == 0)
      h = h + 1;
   end;   
   if (h ~= 0) 
      i = i-h;
      %break;
     %result = create(temp, list, pos, i-h, n);
   else   
      while ((pos(i) > i) & (bitget(temp, pos(i) - 1) ~= 0))
         temp = bitset(temp, pos(i), 1);
         temp = bitset(temp, pos(i)-1, 0);
         list(size(list,2)+1) = temp;
         pos(i) = pos(i) - 1;
      end;   
      %result = create(temp, list, pos, i, n);
   end;   
elseif (i < n)
   for k = 1:i
      temp = bitset(temp,k,1);
   end;
   for k = 1:i
      temp = bitset(temp,pos(i+1)-2-i+k,0);
      pos(k) = pos(i+1)-2-i+k;
   end;   
   i = i+1;
   %result = create(temp, list, pos, i+1, n);
end;
%   result = list;
%end;   
   
end;
result = list;
