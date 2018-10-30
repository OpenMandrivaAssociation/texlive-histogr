# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/histogr
# catalog-date 2006-11-09 15:16:55 +0100
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-histogr
Version:	1.01
Release:	11
Summary:	Draw histograms with the LaTeX picture environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/histogr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/histogr.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.01-2
+ Revision: 752580
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.01-1
+ Revision: 718619
- texlive-histogr
- texlive-histogr
- texlive-histogr
- texlive-histogr

