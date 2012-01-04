# revision 24066
# category Package
# catalog-ctan /macros/latex/contrib/nowidow
# catalog-date 2011-09-21 22:10:12 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-nowidow
Version:	1.0
Release:	2
Summary:	Avoid widows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nowidow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
