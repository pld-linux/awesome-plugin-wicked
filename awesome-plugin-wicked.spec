Summary:	wicked - a lua library for dynamic widgets in awesome
Summary(hu.UTF-8):	wicked - egy lua könyvtár dinamikus widget-ekhez awesome ablakkezelőben
Name:		awesome-plugin-wicked
Version:	20090314
Release:	1
License:	GPL v2
Group:		X11/Window Managers
## git clone git://git.glacicle.com/awesome/wicked.git
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.bz2
# Source0-md5:	4f63b5923180989a35868c1b7b280301
Obsoletes:	wicked
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wicked is a library, written in lua, for easy creation and management
of dynamic awesome statusbar widgets, from the rc.lua configuration
file.

%description -l hu.UTF-8
Wicked egy lua-ban írt könyvtár az awesome statusbar-jában levő
widgetek könnyű létrehozásához és menedzselése az rc.lua konfigurációs
fájlból.

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
# XXX parent dir deps missing
%{_datadir}/awesome/lib/wicked.lua
%{_mandir}/man7/wicked.7*
