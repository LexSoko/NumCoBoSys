%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Sucht nach erlaubten Zuständen
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function result = such(list, z, a, b);

c = floor((a + b) / 2);

if (list(b) == z)
   c = b;
elseif (list(a) == z)  
   c = a;
else
   while ((list(c) ~= z) & (b - a > 1))
      if (z<list(c))
         b = c;
      else  
         a = c;
      end;  
      c = floor((a + b) / 2); 
      if (list(b) == z)
         c = b;
      elseif (list(a) == z)  
         c = a;
      end;  
   end;  
end;

if (z == list(c))
   result = c;
else  
   result = 0;
end;  




%c = floor((a + b)/2);
%if ((a == b) & (z ~= list(c)))
%  result = 0;
%elseif (z<list(c))
%  result = such(list, z, a, c);
%elseif (z>list(c))  
%  result = such(list, z, c, b);
%elseif (z==list(c))  
%  result = c;
%else  
%  result = 0;
%end;  
  