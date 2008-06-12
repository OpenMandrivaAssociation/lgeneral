%define	name	lgeneral
%define	version	1.2
%define	dvers	1.1.3
%define	release	0.beta10.2
%define	Summary	A Panzer General clone

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
Source0:	%{name}-%{version}beta-2.tar.bz2
Source1:	%{name}-data-%{dvers}.tar.bz2
Patch0:		%{name}-1.1.1-reset-player.patch.bz2
License:	GPLv2+
Group:		Games/Strategy
Summary:	%{Summary}
BuildRequires:	SDL_mixer-devel X11-devel nas-devel smpeg-devel oggvorbis-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
You play single scenarios or whole campaigns turn by turn against a human
player or the AI. Entrenchment, rugged defense, defensive fire, surprise
contacts, surrender, unit supply, weather influence, reinforcements and other
implementations contribute to the tactical and strategic depth of the game.
 
%prep
%setup -q -a1 -n %{name}-%{version}beta-2
%patch0 -p1 -b .peroyvind

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make CFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags`"
(cd %{name}-data-%{dvers}; %configure)

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}
(cd %{name}-data-%{dvers}; %makeinstall_std)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}		
Icon=%{name}				
Categories=Game;StrategyGame;		
Name=LGeneral
Comment=%{Summary}
EOF

%{__install} -m644 %{name}16.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} -m644 %{name}32.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} -m644 %{name}48.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man[16]/*
%defattr(755,root,root,755)
%{_gamesbindir}/*

