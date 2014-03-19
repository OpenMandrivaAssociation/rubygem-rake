%define rbname   rake

Summary:    Simple ruby build program with capabilities similar to make
Name:       rubygem-%{rbname}
Version:    10.0.4
Release:    1
License:    MIT
Group:      Development/Ruby
URL:        http://rake.rubyforge.org/
Source0:    http://rubygems.org/downloads/%{rbname}-%{version}.gem
BuildArch:  noarch
BuildRequires: rubygems
BuildRequires: p7zip

%description
This package contains Rake, a simple ruby build program with capabilities
similar to make.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man1/
# use 7z and not gzip, as the file is corrupted.
# For some reason it works fine with 7z.
7z e doc/%{rbname}.1.gz 
install %{rbname}.1 %{buildroot}%{_mandir}/man1/rake.1

%files
%{_bindir}/rake
%{_mandir}/man1/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rake
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/contrib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/contrib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/ext
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/ext/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/loaders
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/rake/loaders/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/CHANGES
%{ruby_gemdir}/gems/%{rbname}-%{version}/MIT-LICENSE
%{ruby_gemdir}/gems/%{rbname}-%{version}/TODO
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/*.rdoc
%{ruby_gemdir}/gems/%{rbname}-%{version}/doc/release_notes/*.rdoc
