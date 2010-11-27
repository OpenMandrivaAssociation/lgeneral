%define	name	lgeneral
%define	version	1.2
%define	release	%mkrel 1
%define	Summary	A Panzer General clone

Name:		%{name}
Version:	%{version}
Summary:	%{Summary}
Release:	%{release}
URL:		http://lgames.sourceforge.net/index.php?project=LGeneral
Source0:	http://prdownloads.sourceforge.net/lgeneral/%{name}-%{version}.tar.gz
Source1:	http://prdownloads.sourceforge.net/lgeneral/pg-data.tar.gz
Patch0:     lgeneral-1.2-fix-format-errors.patch
Patch1:     lgeneral-1.2-as-needed.patch
Patch2:     lgeneral-1.2-build.patch
Patch3:     lgeneral-1.2_beta13-make-382.patch
Patch4:     lgeneral-1.2-make-lgc-pg-buildroot-aware.patch
License:	GPLv2+
Group:		Games/Strategy
BuildRequires:	SDL_mixer-devel
BuildRequires:	X11-devel
BuildRequires:	nas-devel
BuildRequires:	smpeg-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	x11-server-xvfb
BuildRequires:	gettext-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer General.
You play single scenarios or whole campaigns turn by turn against a human
player or the AI. Entrenchment, rugged defense, defensive fire, surprise
contacts, surrender, unit supply, weather influence, reinforcements and other
implementations contribute to the tactical and strategic depth of the game.
 
%prep
%setup -q -a1
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
%patch3 -p 0
%patch4 -p 1
cp /usr/share/gettext/config.rpath .
autoreconf -i -f

%build
%configure2_5x	--bindir=%{_gamesbindir}
%__make CFLAGS="$RPM_OPT_FLAGS `sdl-config --cflags`"

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%find_lang lgeneral
%find_lang pg
cat lgeneral.lang pg.lang > all.lang

# install data files
xvfb-run lgc-pg/lgc-pg -s pg-data -d %{buildroot}%{_gamesdatadir}/lgeneral

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f all.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README* TODO
%{_gamesdatadir}/%{name}
%{_iconsdir}/%{name}48.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man[16]/*
%{_gamesbindir}/*

