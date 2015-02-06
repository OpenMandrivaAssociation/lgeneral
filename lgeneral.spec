Name:		lgeneral
Version:	1.2.3
Summary:	A Panzer General clone
Release:	2
License:	GPLv2+
Group:		Games/Strategy
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
Source0:	http://prdownloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/lgeneral/pg-data.tar.gz
Patch0:		lgeneral-1.2.2-fix-format-errors.patch
Patch4:		lgeneral-1.2-make-lgc-pg-buildroot-aware.patch
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	gettext-devel
BuildRequires:	x11-server-xvfb
BuildRequires:	desktop-file-utils

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
You play single scenarios or whole campaigns turn by turn against a human
player or the AI. Entrenchment, rugged defense, defensive fire, surprise
contacts, surrender, unit supply, weather influence, reinforcements and other
implementations contribute to the tactical and strategic depth of the game.

%prep
%setup -q -a1
%patch0 -p1
%patch4 -p1

%build
cp /usr/share/gettext/config.rpath .
autoreconf -fi
%configure2_5x	--bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
%makeinstall_std

mv %{buildroot}%{_gamesdatadir}/applications %{buildroot}%{_datadir}/
mv %{buildroot}%{_gamesdatadir}/icons %{buildroot}%{_datadir}/

desktop-file-install	--dir %{buildroot}%{_datadir}/applications \
			--add-category="StrategyGame" \
			%{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i s,Icon=.*,Icon=lgeneral48, %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang lgeneral pg %{name}.lang

# not created by make install with new automake but needed for lgc-pg
mkdir -p %{buildroot}%{_gamesdatadir}/lgeneral/gfx/flags
mkdir -p %{buildroot}%{_gamesdatadir}/lgeneral/gfx/terrain
mkdir -p %{buildroot}%{_gamesdatadir}/lgeneral/gfx/units
# install data files
xvfb-run lgc-pg/lgc-pg -s pg-data -d %{buildroot}%{_gamesdatadir}/lgeneral

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README* TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}48.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man[16]/*
%{_gamesbindir}/*



%changelog
* Mon Dec 19 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2.2-2mdv2012.0
+ Revision: 743776
- Fix .desktop file

* Wed Dec 14 2011 Andrey Bondrov <abondrov@mandriva.org> 1.2.2-1
+ Revision: 740881
- New version 1.2.2, drop applied in upstream patches, update patch0

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.2-2
+ Revision: 636022
- tighten BR

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2011.0
+ Revision: 602113
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.2-0.beta10.2mdv2009.0
+ Revision: 218422
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 1.2-0.beta10.2mdv2008.1
+ Revision: 157782
- fix desktop entry

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1.2-0.beta10.1mdv2008.1
+ Revision: 132984
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import lgeneral


* Fri Dec 23 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2-0.beta10.1mdk
- 1.2 beta10
- %%mkrel

* Thu Aug 26 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-0.beta2.2mdk
- rebuild for new menu

* Fri Feb 27 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2-0.beta2.1mdk
- 1.2beta-2
- fix buildrequires(lib64..)
- compile with $RPM_OPT_FLAGS

* Wed Aug 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.1-2mdk
- change summary macro to avoid possible conflicts if we were to build
  debug package
- fix segfault after choosing broken "Torch" scenario (P0, fixes #4654,
  though Torch scenarion will still not work for now..)

* Thu Apr 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.1-1mdk
- initial mdk release
