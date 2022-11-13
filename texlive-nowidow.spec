Name:		texlive-nowidow
Version:	24066
Release:	1
Summary:	Avoid widows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nowidow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a useful macro to manage widow lines.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nowidow/nowidow.sty
%doc %{_texmfdistdir}/doc/latex/nowidow/README
%doc %{_texmfdistdir}/doc/latex/nowidow/nowidow.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nowidow/nowidow.dtx
%doc %{_texmfdistdir}/source/latex/nowidow/nowidow.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
