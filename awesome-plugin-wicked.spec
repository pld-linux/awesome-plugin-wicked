Summary:	wicked - a lua library for dynamic widgets in awesome
Summary(hu.UTF-8):	wicked - egy lua könyvtár dinamikus widget-ekhez awesome ablakkezelőben
Summary(pl.UTF-8):	wicked - biblioteka lua do dynamicznych widgetów w awesome
Name:		awesome-plugin-wicked
Version:	20090428
Release:	2
License:	GPL v2
Group:		X11/Window Managers/Tools
## git clone git://git.glacicle.com/awesome/wicked.git
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	8e00dcf439988c83c3df9642527dd403
Obsoletes:	wicked
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wicked is a library, written in lua, for easy creation and management
of dynamic awesome statusbar widgets, from the rc.lua configuration
file.

%description -l hu.UTF-8
Wicked egy lua-ban írt könyvtár az awesome statusbar-jában levő
widgetek könnyű létrehozásához és menedzselése az rc.lua konfigurációs
fájlból.

%description -l pl.UTF-8
Wicked jest biblioteką języka lua służącą do łatwego tworzenia i
zarządzania dynamicznymi obiektami na paskach statusu zarządcy okien
awesome z poziomu pliku konfiguracyjnego rc.lua.

%prep
%setup -q -n wicked
%{__gzip} -d wicked.7.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install -d $RPM_BUILD_ROOT%{_mandir}/man7
install wicked.lua $RPM_BUILD_ROOT%{_datadir}/awesome/lib
install wicked.7 $RPM_BUILD_ROOT%{_mandir}/man7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/awesome/lib/wicked.lua
%{_mandir}/man7/wicked.7*
