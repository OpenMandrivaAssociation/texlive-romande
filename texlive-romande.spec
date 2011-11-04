# revision 19537
# category Package
# catalog-ctan /fonts/romandeadf
# catalog-date 2010-07-14 23:31:19 +0200
# catalog-license lppl
# catalog-version 1.008-v7
Name:		texlive-romande
Version:	1.008-v7
Release:	1
Summary:	Romande ADF fonts and LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/romandeadf
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romande.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romande.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/romande.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Romande ADF is a serif font family with oldstyle figures,
designed as a substitute for Times, Tiffany or Caslon. The
family currently includes upright, italic and small-caps shapes
in each of regular and demi-bold weights and an italic script
in regular. The support package renames the fonts according to
the Karl Berry fontname scheme and defines four families. Two
of these primarily provide access to the "standard" or default
characters while the "alternate" families support alternate
characters, additional ligatures and the long s. The included
package files provide access to these features in LaTeX as
explained in the documentation. The LaTeX support requires the
nfssext-cfr and the xkeyval packages.

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
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdd8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrddc8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrddi8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdrc8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdri8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/romande/yrdriw8a.afm
%{_texmfdistdir}/fonts/enc/dvips/romande/romande-supp.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/t1-romandeadf-alt.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/t1-romandeadf.enc
%{_texmfdistdir}/fonts/enc/dvips/romande/ts1-euro-yrd.enc
%{_texmfdistdir}/fonts/map/dvips/romande/yrd.map
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/s-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-alt-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrddc.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdrc.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/t1-romandeadf-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdd.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrddi.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdr.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdri.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/ts1-yrdriw.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdd8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdd8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdda8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddai8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrddi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdra8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdrai8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdraiw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdrc8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdriw8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/romande/yrdriw8t.tfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdd8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdd8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddc8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddc8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddi8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrddi8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdr8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdrc8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdrc8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdri8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdri8a.pfm
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdriw8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/romande/yrdriw8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdd8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdd8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdda8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddai8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddi8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrddi8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdra8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdrai8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdraiw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdrc8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdri8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdri8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdriw8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/romande/yrdriw8t.vf
%{_texmfdistdir}/tex/latex/romande/romande.sty
%{_texmfdistdir}/tex/latex/romande/t1yrd.fd
%{_texmfdistdir}/tex/latex/romande/t1yrda.fd
%{_texmfdistdir}/tex/latex/romande/t1yrdaw.fd
%{_texmfdistdir}/tex/latex/romande/t1yrdw.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrd.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrda.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrdaw.fd
%{_texmfdistdir}/tex/latex/romande/ts1yrdw.fd
%doc %{_texmfdistdir}/doc/fonts/romande/COPYING
%doc %{_texmfdistdir}/doc/fonts/romande/NOTICE.txt
%doc %{_texmfdistdir}/doc/fonts/romande/README
%doc %{_texmfdistdir}/doc/fonts/romande/manifest.txt
%doc %{_texmfdistdir}/doc/fonts/romande/romandeadf.pdf
%doc %{_texmfdistdir}/doc/fonts/romande/romandeadf.tex
#- source
%doc %{_texmfdistdir}/source/fonts/romande/reglyph-yrd.tex
%doc %{_texmfdistdir}/source/fonts/romande/romande-supp.etx
%doc %{_texmfdistdir}/source/fonts/romande/t1-romandeadf-alt.etx
%doc %{_texmfdistdir}/source/fonts/romande/t1-romandeadf.etx
%doc %{_texmfdistdir}/source/fonts/romande/ts1-euro.etx
%doc %{_texmfdistdir}/source/fonts/romande/yrd-drv.tex
%doc %{_texmfdistdir}/source/fonts/romande/yrd-map.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
