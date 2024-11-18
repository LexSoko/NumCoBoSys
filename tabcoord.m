%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%  Erzeugt Gitterplatztabelle und n�chste Nachbarliste
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [lattice, nn] = tabcoord(Nx, Ny, periodic)

N = Nx * Ny;

lattice = zeros(N, 2);

einsx = ones(1, Nx);
einsy = ones(1, Ny);
xvek = (1:1:Nx);
yvek = (1:1:Ny);
lattice(:,1) = reshape ((xvek' * einsy), N, 1);
lattice(:,2) = reshape ((einsx' * yvek), N, 1);

clear einsx einsy xvek yvek;

cntnn = 0;

if (~periodic)
 
  for n = 1:Ny
    for m = 1:Nx
      if (m < Nx)
        cntnn = cntnn + 1;
        nn(cntnn, 1) = (n-1) * Nx + m;
        nn(cntnn, 2) = (n-1) * Nx + m + 1;
      end;  
      if (n < Ny)
	cntnn = cntnn + 1;
	nn(cntnn, 1) = (n-1) * Nx + m;
	nn(cntnn, 2) = n * Nx + m;
      end;     
    end;
  end;  
  
elseif (Ny>1)  
  
  for n = 1:Ny
    for m = 1:Nx
      cntnn = cntnn + 1;
      nn(cntnn, 1) = (n-1) * Nx + m;
      nn(cntnn, 2) = (n-1) * Nx + m + 1 - floor(m/Nx) * Nx;
      cntnn = cntnn + 1;
      nn(cntnn, 1) = (n-1) * Nx + m;
      nn(cntnn, 2) = n * Nx + m - floor(n/Ny) * Ny * Nx;
    end;  
  end;  
  
else
  
  for m = 1:Nx
    cntnn = cntnn + 1;
    nn(cntnn, 1) = m;
    nn(cntnn, 2) = m + 1 - floor(m/Nx) * Nx;
  end;  
  
end;  

plot(lattice(:,1), lattice(:,2),'*');
%axis([0 Nx+1 0 Ny+1]); 