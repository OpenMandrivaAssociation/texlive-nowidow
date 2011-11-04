# revision 24066
# category Package
# catalog-ctan /macros/latex/contrib/nowidow
# catalog-date 2011-09-21 22:10:12 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-nowidow
Version:	1.0
Release:	1
Summary:	Avoid widows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nowidow
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nowidow.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package provides a useful macro to manage widow lines.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nowidow/nowidow.sty
%doc %{_texmfdistdir}/doc/latex/nowidow/README
%doc %{_texmfdistdir}/doc/latex/nowidow/nowidow.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nowidow/nowidow.dtx
%doc %{_texmfdistdir}/source/latex/nowidow/nowidow.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
