%global tl_name nowidow
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Avoid widows
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nowidow
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a useful macro to manage widow lines.

