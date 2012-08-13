# revision 27331
# category Package
# catalog-ctan /macros/latex/contrib/opteng
# catalog-date 2012-06-16 14:32:26 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-opteng
Version:	1.0
Release:	1
Summary:	SPIE Optical Engineering and OE Letters manuscript template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/opteng
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opteng.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opteng.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
With this template, and associated style and LaTeX packages, it
is possible to estimate the page length of manuscripts for
submission to the SPIE journals 'Optical Engineering' and
'Optical Engineering Letters'. With a strict three-page limit,
this is particularly important for the latter. The template
gives simple instructions on how to prepare the manuscript.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/opteng/opteng.sty
%doc %{_texmfdistdir}/doc/latex/opteng/OptEngInstruct.pdf
%doc %{_texmfdistdir}/doc/latex/opteng/OptEngInstruct.tex
%doc %{_texmfdistdir}/doc/latex/opteng/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
