# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/histogr
# catalog-date 2006-11-09 15:16:55 +0100
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-histogr
Version:	1.01
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This is a macro collection to draw histogram bars inside a
LaTeX picture-environment.

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
%{_texmfdistdir}/tex/latex/histogr/histogr.sty
%doc %{_texmfdistdir}/doc/latex/histogr/histogr.pdf
#- source
%doc %{_texmfdistdir}/source/latex/histogr/histogr.dtx
%doc %{_texmfdistdir}/source/latex/histogr/histogr.ins
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
