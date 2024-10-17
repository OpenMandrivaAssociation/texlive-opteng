Name:		texlive-opteng
Version:	27331
Release:	2
Summary:	SPIE Optical Engineering and OE Letters manuscript template
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/opteng
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opteng.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/opteng.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
