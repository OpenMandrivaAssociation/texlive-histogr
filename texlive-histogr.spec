Name:		texlive-histogr
Version:	15878
Release:	2
Summary:	Draw histograms with the LaTeX picture environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/histogr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a macro collection to draw histogram bars inside a
LaTeX picture-environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/histogr/histogr.sty
%doc %{_texmfdistdir}/doc/latex/histogr/histogr.pdf
#- source
%doc %{_texmfdistdir}/source/latex/histogr/histogr.dtx
%doc %{_texmfdistdir}/source/latex/histogr/histogr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
